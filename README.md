# NutriVision Pro - AI-Powered Food Analyzer

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.0+-000000?style=for-the-badge&logo=flask&logoColor=white)
![Google AI](https://img.shields.io/badge/Google%20Gemini-AI-4285F4?style=for-the-badge&logo=google&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-Cloud-47A248?style=for-the-badge&logo=mongodb&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**Advanced AI-powered nutrition analysis and meal planning platform**

[Features](#features) • [Demo](#demo) • [Installation](#installation) • [Usage](#usage) • [API](#api) • [Contributing](#contributing)

</div>

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Architecture](#architecture)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Project Structure](#project-structure)
- [Screenshots](#screenshots)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Overview

NutriVision Pro is a cutting-edge web application that leverages Google's Gemini AI to provide comprehensive nutritional analysis of food items through image recognition. Simply upload a photo of your food, and get instant, detailed nutritional information including calories, macronutrients, vitamins, health benefits, and more.

### Key Highlights

- **AI-Powered Analysis**: Utilizes Google Gemini 2.5 Flash for accurate food identification
- **Comprehensive Data**: Provides detailed nutritional breakdown per 100g
- **Health Insights**: Offers health benefits, allergen information, and dietary classifications
- **Cloud Storage**: Stores analysis history in MongoDB for future reference
- **Modern UI/UX**: Beautiful, responsive interface with smooth animations
- **Real-time Processing**: Fast image upload and analysis with progress tracking

---

## Features

### Core Functionality

#### Food Analysis
- **Image Recognition**: Upload food images in JPG, PNG, GIF, BMP, or WebP formats
- **Nutritional Breakdown**: Complete macronutrient and micronutrient information
- **Calorie Calculation**: Accurate calorie estimation per 100g
- **Vitamin & Mineral Content**: Detailed vitamin and mineral analysis

#### Health Information
- **Health Benefits**: Key health advantages of the identified food
- **Allergen Detection**: Identification of potential allergens
- **Dietary Classifications**: Vegan, Vegetarian, Gluten-free, etc.
- **Glycemic Index**: Low/Medium/High classification
- **Storage Tips**: Recommendations for proper food storage
- **Preparation Suggestions**: Cooking and preparation methods

#### User Experience
- **Drag & Drop Upload**: Intuitive file upload interface
- **Progress Tracking**: Real-time upload and analysis progress
- **Analysis History**: View past food analyses (up to 50 recent items)
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile
- **Error Handling**: Comprehensive error messages and validation

### Planned Features

- **Meal Planner**: Create personalized weekly meal plans
- **Nutrition Chatbot**: AI assistant for nutrition queries
- **Diet Expert Consultation**: Professional dietary advice
- **Export Functionality**: PDF/CSV export of analysis results
- **User Authentication**: Personalized user accounts
- **Dark Mode**: Toggle between light and dark themes

---

## Technology Stack

### Backend
- **Framework**: Flask 2.0+
- **Language**: Python 3.8+
- **AI Model**: Google Gemini 2.5 Flash
- **Database**: MongoDB (Cloud)
- **Image Processing**: Pillow (PIL)
- **Environment**: python-dotenv

### Frontend
- **HTML5**: Semantic markup
- **CSS3**: Modern styling with animations
- **JavaScript**: Vanilla JS (ES6+)
- **Icons**: Font Awesome 6.4.0
- **Fonts**: Google Fonts (Poppins)

### Infrastructure
- **Server**: Flask Development Server (Development)
- **Database**: MongoDB Atlas (Cloud)
- **API**: Google Generative AI API
- **Storage**: MongoDB GridFS (Base64 images)

---

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      Client Browser                          │
│  ┌───────────────┐  ┌───────────────┐  ┌───────────────┐   │
│  │  Landing Page │  │   Dashboard   │  │   404 Page    │   │
│  │  (index.html) │  │ (dashboard.   │  │  (404.html)   │   │
│  │               │  │     html)     │  │               │   │
│  └───────┬───────┘  └───────┬───────┘  └───────────────┘   │
└──────────┼──────────────────┼──────────────────────────────┘
           │                  │
           │ HTTP Request     │ AJAX Request
           │                  │
┌──────────▼──────────────────▼──────────────────────────────┐
│                    Flask Application                         │
│  ┌────────────────────────────────────────────────────────┐ │
│  │              Route Handlers (app.py)                   │ │
│  │  • / (index)    • /dashboard    • /upload             │ │
│  │  • /history     • /analysis     • /delete             │ │
│  └────────┬───────────────────────┬───────────────────────┘ │
│           │                       │                          │
│  ┌────────▼─────────┐    ┌───────▼──────────┐              │
│  │ Image Processing │    │  Data Processing │              │
│  │  • Base64 encode │    │  • JSON parsing  │              │
│  │  • Validation    │    │  • Sanitization  │              │
│  └────────┬─────────┘    └──────────────────┘              │
└───────────┼──────────────────────────────────────────────────┘
            │
            │ API Call
            │
┌───────────▼──────────────────────────────────────────────────┐
│              Google Gemini AI (gemini-2.5-flash)             │
│  • Image Analysis        • Nutritional Data Extraction       │
│  • Food Identification   • Health Information Generation     │
└───────────┬──────────────────────────────────────────────────┘
            │
            │ Store/Retrieve
            │
┌───────────▼──────────────────────────────────────────────────┐
│                    MongoDB Atlas (Cloud)                      │
│  • Food Analysis Records    • Base64 Image Storage           │
│  • User Sessions            • Timestamps                     │
└──────────────────────────────────────────────────────────────┘
```

---

## Installation

### Prerequisites

- Python 3.8 or higher
- MongoDB Atlas account (or local MongoDB instance)
- Google Gemini API key
- Git (optional)

### Step 1: Clone the Repository

```bash
git clone https://github.com/pranavsoftware/nutrivision-pro.git
cd nutrivision-pro
```

### Step 2: Create Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Set Up Environment Variables

Create a `.env` file in the project root:

```env
# Flask Configuration
FLASK_SECRET_KEY=your-secret-key-change-this-in-production
FLASK_DEBUG=True
FLASK_HOST=0.0.0.0
FLASK_PORT=5000

# Google Gemini AI Configuration
GEMINI_API_KEY=your-gemini-api-key-here

# MongoDB Configuration
MONGODB_URI=your-mongodb-connection-string
DATABASE_NAME=food_analyzer
COLLECTION_NAME=food_items

# File Upload Configuration
MAX_CONTENT_LENGTH=16777216
```

### Step 5: Get API Keys

#### Google Gemini API Key:
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Create a new API key
4. Copy the key to your `.env` file

#### MongoDB Atlas:
1. Visit [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
2. Create a free cluster
3. Create a database user
4. Whitelist your IP address
5. Get the connection string
6. Replace `<password>` with your database user password
7. Add the connection string to your `.env` file

### Step 6: Run the Application

```bash
python app.py
```

Visit `http://localhost:5000` in your browser.

---

## Configuration

### Environment Variables

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `FLASK_SECRET_KEY` | Secret key for Flask sessions | - | Yes |
| `FLASK_DEBUG` | Enable debug mode | `False` | No |
| `FLASK_HOST` | Host address | `0.0.0.0` | No |
| `FLASK_PORT` | Port number | `5000` | No |
| `GEMINI_API_KEY` | Google Gemini API key | - | Yes |
| `MONGODB_URI` | MongoDB connection string | - | Yes |
| `DATABASE_NAME` | MongoDB database name | `food_analyzer` | No |
| `COLLECTION_NAME` | MongoDB collection name | `food_items` | No |
| `MAX_CONTENT_LENGTH` | Max upload size (bytes) | `16777216` (16MB) | No |

### Supported File Formats

- JPEG/JPG
- PNG
- GIF
- BMP
- WebP

Maximum file size: 16MB

---

## Usage

### Basic Workflow

1. **Launch Application**: Start the Flask server
2. **Access Landing Page**: Navigate to `http://localhost:5000`
3. **Click "Start Scanning"**: Opens the food analyzer dashboard
4. **Upload Image**: 
   - Click "Choose File" to select an image
   - Or drag and drop an image onto the upload area
5. **Wait for Analysis**: AI processes the image (typically 3-5 seconds)
6. **View Results**: Comprehensive nutritional information displays
7. **Analyze More**: Click "Analyze Another Image" to continue

### Advanced Features

#### View Analysis History
```
GET /history
```
Returns the last 50 food analyses with timestamps.

#### Get Specific Analysis
```
GET /analysis/<analysis_id>
```
Retrieves a specific analysis by MongoDB ObjectId.

#### Delete Analysis
```
DELETE /delete/<analysis_id>
```
Removes a specific analysis from the database.

---

## API Documentation

### Endpoints

#### `POST /upload`

Upload and analyze a food image.

**Request:**
- Content-Type: `multipart/form-data`
- Body: `file` (image file)

**Response:**
```json
{
  "success": true,
  "food_data": {
    "food_name": "Apple",
    "category": "Fruit",
    "calories_per_100g": "52",
    "nutritional_info": {
      "protein": "0.3",
      "carbohydrates": "14",
      "fat": "0.2",
      "fiber": "2.4",
      "sugar": "10",
      "sodium": "1"
    },
    "vitamins_minerals": { ... },
    "health_benefits": [ ... ],
    "allergens": [ ... ],
    "storage_tips": "...",
    "preparation_suggestions": [ ... ],
    "serving_size": "1 medium apple (182g)",
    "glycemic_index": "Low",
    "dietary_restrictions": ["Vegan", "Vegetarian", "Gluten-free"]
  },
  "image_base64": "data:image/jpeg;base64,...",
  "original_filename": "apple.jpg"
}
```

#### `GET /history`

Retrieve analysis history.

**Response:**
```json
{
  "success": true,
  "analyses": [
    {
      "_id": "...",
      "timestamp": "2025-10-15 11:30:00",
      "original_filename": "apple.jpg",
      "food_data": { ... },
      "image_preview": "data:image/jpeg;base64,..."
    }
  ]
}
```

#### `GET /analysis/<analysis_id>`

Get specific analysis by ID.

**Response:**
```json
{
  "success": true,
  "analysis": { ... }
}
```

#### `DELETE /delete/<analysis_id>`

Delete specific analysis.

**Response:**
```json
{
  "success": true,
  "message": "Analysis deleted successfully"
}
```

### Error Responses

```json
{
  "success": false,
  "error": "Error message description"
}
```

**Common Error Codes:**
- `400`: Bad Request (no file, invalid format)
- `404`: Not Found (analysis not found)
- `413`: File Too Large (exceeds 16MB)
- `500`: Internal Server Error

---

## Project Structure

```
nutrivision-pro/
├── app.py                          # Main Flask application
├── requirements.txt                # Python dependencies
├── .env                           # Environment variables (not in repo)
├── .env.example                   # Example environment file
├── .gitignore                     # Git ignore rules
├── README.md                      # This file
├── UPDATES.md                     # Update documentation
├── STATIC_FILES_STRUCTURE.md      # Static files documentation
│
├── static/                        # Static assets
│   ├── css/
│   │   ├── dashboard.css          # Landing page styles
│   │   └── analyzer.css           # Analyzer page styles
│   └── js/
│       └── dashboard.js           # Frontend JavaScript
│
├── templates/                     # HTML templates
│   ├── index.html                 # Landing page
│   ├── dashboard.html             # Food analyzer interface
│   └── 404.html                   # Error page
│
└── uploads/                       # Temporary upload directory
```

---

## Screenshots

### Landing Page
![Landing Page](https://via.placeholder.com/800x450/667eea/ffffff?text=NutriVision+Pro+Landing+Page)

### Food Analyzer Dashboard
![Analyzer](https://via.placeholder.com/800x450/764ba2/ffffff?text=Food+Analyzer+Dashboard)

### Analysis Results
![Results](https://via.placeholder.com/800x450/667eea/ffffff?text=Nutritional+Analysis+Results)

---

## Deployment

### Production Deployment

#### 1. Using Gunicorn (Recommended)

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

#### 2. Using Docker

Create `Dockerfile`:

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
```

Build and run:

```bash
docker build -t nutrivision-pro .
docker run -p 5000:5000 --env-file .env nutrivision-pro
```

#### 3. Using Heroku

```bash
heroku create nutrivision-pro
heroku config:set GEMINI_API_KEY=your-key
heroku config:set MONGODB_URI=your-uri
git push heroku main
```

### Environment Considerations

- Set `FLASK_DEBUG=False` in production
- Use strong `FLASK_SECRET_KEY`
- Enable HTTPS
- Implement rate limiting
- Add authentication for sensitive endpoints
- Configure CORS properly
- Set up monitoring and logging

---

## Contributing

Contributions are welcome! Please follow these guidelines:

### How to Contribute

1. **Fork the Repository**
   ```bash
   git clone https://github.com/pranavsoftware/nutrivision-pro.git
   ```

2. **Create a Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make Changes**
   - Write clean, documented code
   - Follow PEP 8 style guide for Python
   - Add comments where necessary

4. **Test Your Changes**
   ```bash
   python app.py
   # Test all functionality
   ```

5. **Commit Changes**
   ```bash
   git add .
   git commit -m "Add: your feature description"
   ```

6. **Push to GitHub**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create Pull Request**
   - Go to GitHub
   - Click "New Pull Request"
   - Describe your changes

### Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Focus on what is best for the community
- Show empathy towards other community members

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 Pranav Rayban

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## Contact

### Developer

**Pranav Rayban**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/pranavrayban/)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/pranavsoftware)

### Project Links

- **Repository**: [https://github.com/pranavsoftware/nutrivision-pro](https://github.com/pranavsoftware/nutrivision-pro)
- **Issues**: [https://github.com/pranavsoftware/nutrivision-pro/issues](https://github.com/pranavsoftware/nutrivision-pro/issues)
- **Discussions**: [https://github.com/pranavsoftware/nutrivision-pro/discussions](https://github.com/pranavsoftware/nutrivision-pro/discussions)

---

## Acknowledgments

- **Google Gemini AI**: For powerful image recognition and analysis
- **MongoDB**: For reliable cloud database services
- **Flask**: For the lightweight and flexible web framework
- **Font Awesome**: For beautiful icons
- **Google Fonts**: For the Poppins font family

---

## Changelog

### Version 1.0.0 (2025-10-15)

#### Added
- Initial release
- AI-powered food image analysis
- Comprehensive nutritional breakdown
- MongoDB cloud storage integration
- Responsive web interface
- SVG-based icons and animations
- Error handling and validation
- Analysis history functionality

#### Features
- Upload food images (JPG, PNG, GIF, BMP, WebP)
- Real-time AI analysis with Gemini 2.5 Flash
- Detailed nutritional information
- Health benefits and allergen detection
- Storage tips and preparation suggestions
- Mobile-responsive design
- Custom 404 error page

---

<div align="center">

**Made with dedication by [Pranav Rayban](https://www.linkedin.com/in/pranavrayban/)**

⭐ Star this repository if you find it helpful!

</div>
