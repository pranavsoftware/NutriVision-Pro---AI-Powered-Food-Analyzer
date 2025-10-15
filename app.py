import os
import io
import base64
from flask import Flask, render_template, request, jsonify, flash, redirect, url_for
from werkzeug.utils import secure_filename
import google.generativeai as genai
from pymongo import MongoClient
from datetime import datetime
from PIL import Image
import json
import re
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'fallback-secret-key-for-development')

# Configuration from environment variables
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
MONGODB_URI = os.getenv('MONGODB_URI')
DATABASE_NAME = os.getenv('DATABASE_NAME', 'food_analyzer')
COLLECTION_NAME = os.getenv('COLLECTION_NAME', 'food_items')

# Validate required environment variables
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable is required")
if not MONGODB_URI:
    raise ValueError("MONGODB_URI environment variable is required")

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

# Initialize MongoDB
try:
    client = MongoClient(MONGODB_URI)
    db = client[DATABASE_NAME]
    collection = db[COLLECTION_NAME]
    print("[SUCCESS] MongoDB connected successfully!")
except Exception as e:
    print(f"[ERROR] MongoDB connection error: {e}")

# Configure upload settings
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp', 'webp'}
MAX_CONTENT_LENGTH = int(os.getenv('MAX_CONTENT_LENGTH', 16777216))  # 16MB default

app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def image_to_base64(image_file):
    """Convert uploaded image file to base64 string"""
    try:
        # Read the file content
        image_data = image_file.read()
        # Reset file pointer for further processing
        image_file.seek(0)
        # Convert to base64
        base64_string = base64.b64encode(image_data).decode('utf-8')
        return base64_string
    except Exception as e:
        print(f"Error converting image to base64: {e}")
        return None

def extract_json_from_response(response_text):
    """Extract JSON from Gemini response with multiple fallback methods"""
    # Method 1: Look for JSON code blocks
    json_pattern = r'``````'
    match = re.search(json_pattern, response_text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(1))
        except json.JSONDecodeError:
            pass
    
    # Method 2: Look for any code blocks
    code_pattern = r'``````'
    match = re.search(code_pattern, response_text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(1))
        except json.JSONDecodeError:
            pass
    
    # Method 3: Look for JSON-like structure
    json_start = response_text.find('{')
    json_end = response_text.rfind('}')
    if json_start != -1 and json_end != -1 and json_end > json_start:
        try:
            return json.loads(response_text[json_start:json_end + 1])
        except json.JSONDecodeError:
            pass
    
    # Method 4: Try parsing the entire response
    try:
        return json.loads(response_text.strip())
    except json.JSONDecodeError:
        pass
    
    return None

def analyze_food_with_gemini(image_file):
    """Analyze food image using Gemini API and return structured data"""
    try:
        # Initialize the model
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        # Open and process the image
        img = Image.open(image_file)
        
        # Create a detailed prompt for food analysis
        prompt = """
        Analyze this food image and provide detailed nutritional information in the following JSON format ONLY. 
        Do not include any other text before or after the JSON:

        {
            "food_name": "Name of the food item",
            "category": "Food category (e.g., Fruit, Vegetable, Grain, Protein, Dairy, etc.)",
            "calories_per_100g": "Estimated calories per 100 grams (number only)",
            "nutritional_info": {
                "protein": "Protein content in grams per 100g (number only)",
                "carbohydrates": "Carbohydrate content in grams per 100g (number only)",
                "fat": "Fat content in grams per 100g (number only)",
                "fiber": "Fiber content in grams per 100g (number only)",
                "sugar": "Sugar content in grams per 100g (number only)",
                "sodium": "Sodium content in mg per 100g (number only)"
            },
            "vitamins_minerals": {
                "vitamin_c": "Vitamin C content with units",
                "vitamin_a": "Vitamin A content with units",
                "iron": "Iron content with units",
                "calcium": "Calcium content with units",
                "potassium": "Potassium content with units"
            },
            "health_benefits": ["List of 3-5 key health benefits"],
            "allergens": ["List of potential allergens if any"],
            "storage_tips": "Brief storage recommendation",
            "preparation_suggestions": ["List of 2-3 preparation methods"],
            "serving_size": "Standard serving size",
            "glycemic_index": "Low/Medium/High",
            "dietary_restrictions": ["Applicable dietary categories like Vegan, Vegetarian, Gluten-free, etc."]
        }
        
        Provide accurate nutritional information. If you cannot identify the food clearly, set food_name to "Unidentified food item".
        """
        
        # Generate content using the model
        response = model.generate_content([prompt, img])
        
        # Extract and parse the JSON response
        response_text = response.text.strip()
        
        # Try to extract JSON from response
        food_data = extract_json_from_response(response_text)
        
        if food_data:
            return food_data
        else:
            # Fallback: create a basic structure if JSON parsing fails
            return {
                "food_name": "Unable to identify food item",
                "category": "Unknown",
                "calories_per_100g": "N/A",
                "nutritional_info": {
                    "protein": "N/A",
                    "carbohydrates": "N/A",
                    "fat": "N/A",
                    "fiber": "N/A",
                    "sugar": "N/A",
                    "sodium": "N/A"
                },
                "vitamins_minerals": {
                    "vitamin_c": "N/A",
                    "vitamin_a": "N/A",
                    "iron": "N/A",
                    "calcium": "N/A",
                    "potassium": "N/A"
                },
                "health_benefits": ["Analysis could not be completed"],
                "allergens": [],
                "storage_tips": "Store according to food type",
                "preparation_suggestions": ["Cook as desired"],
                "serving_size": "N/A",
                "glycemic_index": "N/A",
                "dietary_restrictions": [],
                "raw_response": response_text,
                "parsing_error": True
            }
            
    except Exception as e:
        print(f"Error analyzing food with Gemini: {e}")
        return {
            "error": f"Failed to analyze food: {str(e)}",
            "food_name": "Analysis Failed",
            "category": "Unknown",
            "calories_per_100g": "N/A",
            "nutritional_info": {
                "protein": "N/A",
                "carbohydrates": "N/A",
                "fat": "N/A",
                "fiber": "N/A",
                "sugar": "N/A",
                "sodium": "N/A"
            },
            "vitamins_minerals": {},
            "health_benefits": [],
            "allergens": [],
            "storage_tips": "N/A",
            "preparation_suggestions": [],
            "serving_size": "N/A",
            "glycemic_index": "N/A",
            "dietary_restrictions": []
        }

def save_to_mongodb(food_data, image_base64, original_filename):
    """Save food analysis data and base64 image to MongoDB"""
    try:
        document = {
            "timestamp": datetime.now(),
            "original_filename": original_filename,
            "image_base64": image_base64,
            "food_data": food_data,
            "analysis_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "user_session": request.remote_addr  # Track user sessions
        }
        
        result = collection.insert_one(document)
        print(f"[SUCCESS] Document saved to MongoDB with ID: {result.inserted_id}")
        return str(result.inserted_id)
    except Exception as e:
        print(f"[ERROR] Error saving to MongoDB: {e}")
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file selected', 'success': False}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No file selected', 'success': False}), 400
    
    if file and allowed_file(file.filename):
        try:
            # Get original filename
            original_filename = secure_filename(file.filename)
            
            # Convert image to base64
            image_base64 = image_to_base64(file)
            if not image_base64:
                return jsonify({'error': 'Failed to process image', 'success': False}), 500
            
            # Reset file pointer for Gemini analysis
            file.seek(0)
            
            # Analyze the food image with Gemini
            print(f"[INFO] Analyzing image: {original_filename}")
            food_data = analyze_food_with_gemini(file)
            
            # Save to MongoDB with base64 image
            mongo_id = save_to_mongodb(food_data, image_base64, original_filename)
            
            if mongo_id:
                food_data['mongo_id'] = mongo_id
            
            # Return the analysis results
            return jsonify({
                'success': True,
                'food_data': food_data,
                'image_base64': f"data:image/jpeg;base64,{image_base64}",
                'original_filename': original_filename
            })
            
        except Exception as e:
            print(f"[ERROR] Error processing file: {e}")
            return jsonify({'error': f'Error processing file: {str(e)}', 'success': False}), 500
    
    return jsonify({'error': 'Invalid file type. Please upload JPG, PNG, GIF, BMP, or WebP files.', 'success': False}), 400

@app.route('/history')
def history():
    """Get analysis history from MongoDB"""
    try:
        # Get recent analyses (limit to 50)
        analyses = list(collection.find().sort("timestamp", -1).limit(50))
        
        # Convert ObjectId to string for JSON serialization
        for analysis in analyses:
            analysis['_id'] = str(analysis['_id'])
            analysis['timestamp'] = analysis['timestamp'].strftime("%Y-%m-%d %H:%M:%S")
            # Include base64 image for history display
            if 'image_base64' in analysis:
                analysis['image_preview'] = f"data:image/jpeg;base64,{analysis['image_base64']}"
        
        return jsonify({'success': True, 'analyses': analyses})
    except Exception as e:
        print(f"[ERROR] Error fetching history: {e}")
        return jsonify({'error': f'Error fetching history: {str(e)}', 'success': False}), 500

@app.route('/analysis/<analysis_id>')
def get_analysis(analysis_id):
    """Get specific analysis by ID"""
    try:
        from bson import ObjectId
        analysis = collection.find_one({"_id": ObjectId(analysis_id)})
        
        if analysis:
            analysis['_id'] = str(analysis['_id'])
            analysis['timestamp'] = analysis['timestamp'].strftime("%Y-%m-%d %H:%M:%S")
            if 'image_base64' in analysis:
                analysis['image_preview'] = f"data:image/jpeg;base64,{analysis['image_base64']}"
            return jsonify({'success': True, 'analysis': analysis})
        else:
            return jsonify({'error': 'Analysis not found', 'success': False}), 404
    except Exception as e:
        print(f"[ERROR] Error fetching analysis: {e}")
        return jsonify({'error': f'Error fetching analysis: {str(e)}', 'success': False}), 500

@app.route('/delete/<analysis_id>', methods=['DELETE'])
def delete_analysis(analysis_id):
    """Delete specific analysis by ID"""
    try:
        from bson import ObjectId
        result = collection.delete_one({"_id": ObjectId(analysis_id)})
        
        if result.deleted_count > 0:
            return jsonify({'success': True, 'message': 'Analysis deleted successfully'})
        else:
            return jsonify({'error': 'Analysis not found', 'success': False}), 404
    except Exception as e:
        print(f"[ERROR] Error deleting analysis: {e}")
        return jsonify({'error': f'Error deleting analysis: {str(e)}', 'success': False}), 500

@app.errorhandler(413)
def too_large(e):
    return jsonify({'error': 'File too large. Maximum size is 16MB.', 'success': False}), 413

if __name__ == '__main__':
    print("[INFO] Starting Food Analyzer Application...")
    
    # Get configuration from environment variables
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    host = os.getenv('FLASK_HOST', '0.0.0.0')
    port = int(os.getenv('FLASK_PORT', 5000))
    
    print(f"[INFO] Access the app at: http://{host}:{port}")
    app.run(debug=debug_mode, host=host, port=port)
