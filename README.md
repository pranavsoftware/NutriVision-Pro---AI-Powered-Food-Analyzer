# NutriVision Pro - AI-Powered Food Analyzer

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.0+-000000?style=for-the-badge&logo=flask&logoColor=white)
![Google AI](https://img.shields.io/badge/Google%20Gemini-AI-4285F4?style=for-the-badge&logo=google&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-Cloud-47A248?style=for-the-badge&logo=mongodb&logoColor=white)

**Advanced AI nutrition analysis and meal planning platform powered by Google Gemini**

[Features](#-features) • [Demo](#-screenshots) • [Installation](#-installation) • [Usage](#-usage) • [API](#-api-reference) • [Deploy](#-deployment)

</div>

---

## Overview

NutriVision Pro leverages Google's Gemini AI to deliver comprehensive nutritional analysis through image recognition. Upload a food photo and instantly receive detailed nutritional breakdowns, health insights, allergen information, and dietary recommendations.

### Key Capabilities

- **AI-Powered Recognition**: Gemini 2.5 Flash for accurate food identification
- **Comprehensive Analysis**: Complete nutritional data per 100g serving
- **Health Intelligence**: Benefits, allergens, dietary classifications, and glycemic index
- **Cloud Storage**: MongoDB Atlas for persistent analysis history
- **Modern Interface**: Responsive design with intuitive user experience

---

## 🎯 Features

### Core Functionality

<table>
<tr>
<td width="50%">

**Image Analysis**
- Multi-format support (JPG, PNG, GIF, BMP, WebP)
- Drag-and-drop upload interface
- Real-time processing with progress tracking
- 16MB maximum file size

</td>
<td width="50%">

**Nutritional Data**
- Calories and macronutrients
- Vitamins and minerals breakdown
- Serving size recommendations
- Glycemic index classification

</td>
</tr>
<tr>
<td width="50%">

**Health Insights**
- Key health benefits
- Allergen detection and warnings
- Dietary restrictions (Vegan, Vegetarian, etc.)
- Storage and preparation tips

</td>
<td width="50%">

**User Experience**
- Analysis history (last 50 items)
- Responsive mobile-first design
- Error handling and validation
- Custom 404 error page

</td>
</tr>
</table>

---

## 📸 Screenshots

### Landing Page - Your Personal Nutrition Assistant
![Landing Page](./food%20analyzer/Sample%20result%201.png)
*Feature overview with multiple nutrition journey options*

### Food Analyzer Dashboard
![Analyzer Dashboard](./food%20analyzer/Sample%20result%202.png)
*Simple drag-and-drop interface for food image upload*

### Comprehensive Analysis Results
![Analysis Results](./food%20analyzer/Sample%20result%203.png)
*Detailed nutritional breakdown with health insights and recommendations*

---

## 🛠️ Technology Stack

<table>
<tr>
<td><strong>Backend</strong></td>
<td>Flask 2.0+, Python 3.8+, Google Gemini 2.5 Flash</td>
</tr>
<tr>
<td><strong>Database</strong></td>
<td>MongoDB Atlas (Cloud)</td>
</tr>
<tr>
<td><strong>Frontend</strong></td>
<td>HTML5, CSS3, Vanilla JavaScript (ES6+)</td>
</tr>
<tr>
<td><strong>Libraries</strong></td>
<td>Pillow (Image Processing), python-dotenv (Config)</td>
</tr>
<tr>
<td><strong>UI/UX</strong></td>
<td>Font Awesome 6.4.0, Google Fonts (Poppins)</td>
</tr>
</table>

---

## 🚀 Installation

### Prerequisites

- Python 3.8+
- MongoDB Atlas account
- Google Gemini API key

### Quick Start

1. **Clone Repository**
```bash
git clone https://github.com/pranavsoftware/nutrivision-pro.git
cd nutrivision-pro
```

2. **Create Virtual Environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure Environment**

Create `.env` file:
```env
FLASK_SECRET_KEY=your-secret-key-here
GEMINI_API_KEY=your-gemini-api-key
MONGODB_URI=your-mongodb-connection-string
DATABASE_NAME=food_analyzer
COLLECTION_NAME=food_items
```

**Get API Keys:**
- **Gemini API**: [Google AI Studio](https://makersuite.google.com/app/apikey)
- **MongoDB**: [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)

5. **Run Application**
```bash
python app.py
```

Visit `http://localhost:5000`

---

## 📖 Usage

### Basic Workflow

1. Access the landing page at `http://localhost:5000`
2. Click "Start Scanning" to open the analyzer
3. Upload food image via click or drag-and-drop
4. Wait for AI analysis (3-5 seconds)
5. Review comprehensive nutritional data
6. Analyze more images or view history

### Project Structure

```
nutrivision-pro/
├── app.py                    # Flask application
├── requirements.txt          # Python dependencies
├── .env                      # Environment variables
├── static/
│   ├── css/
│   │   ├── dashboard.css     # Landing page styles
│   │   └── analyzer.css      # Analyzer styles
│   └── js/
│       └── dashboard.js      # Frontend logic
├── templates/
│   ├── index.html            # Landing page
│   ├── dashboard.html        # Analyzer interface
│   └── 404.html              # Error page
└── uploads/                  # Temporary storage
```

---

## 🔌 API Reference

### Upload & Analyze

```http
POST /upload
```

**Request:**
- Content-Type: `multipart/form-data`
- Body: `file` (image file)

**Response:**
```json
{
  "success": true,
  "food_data": {
    "food_name": "Pav Bhaji",
    "category": "Mixed Dish",
    "calories_per_100g": "180",
    "nutritional_info": {
      "protein": "6g",
      "carbohydrates": "22g",
      "fat": "8g",
      "fiber": "4g"
    },
    "health_benefits": ["Energy source", "Rich in vitamins"],
    "allergens": ["Wheat", "Dairy"],
    "glycemic_index": "High"
  },
  "image_base64": "data:image/jpeg;base64,...",
  "original_filename": "food.jpg"
}
```

### Get History

```http
GET /history
```

Returns last 50 analyses with timestamps and image previews.

### Get Analysis by ID

```http
GET /analysis/<analysis_id>
```

### Delete Analysis

```http
DELETE /delete/<analysis_id>
```

### Error Responses

| Code | Description |
|------|-------------|
| 400 | Bad Request (no file/invalid format) |
| 404 | Analysis not found |
| 413 | File too large (>16MB) |
| 500 | Internal server error |

---

## 🌐 Deployment

### Production Setup

**Using Gunicorn:**
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

**Using Docker:**
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
```

**Environment Checklist:**
- Set `FLASK_DEBUG=False`
- Use strong `FLASK_SECRET_KEY`
- Enable HTTPS
- Implement rate limiting
- Configure CORS policies
- Set up monitoring

---

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

**Guidelines:**
- Follow PEP 8 style guide
- Add comprehensive comments
- Test thoroughly before submitting
- Update documentation as needed

---

## 📄 License

This project is licensed under the MIT License.

```
MIT License - Copyright (c) 2025 Pranav Rayban
See LICENSE file for full details
```

---

## 📬 Contact

**Pranav Rayban**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/pranavrayban/)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=flat-square&logo=github)](https://github.com/pranavsoftware)

**Project Links:**
- Repository: [github.com/pranavsoftware/nutrivision-pro](https://github.com/pranavsoftware/nutrivision-pro)
- Issues: [Report bugs or request features](https://github.com/pranavsoftware/nutrivision-pro/issues)

---

## 🙏 Acknowledgments

- Google Gemini AI for powerful image recognition
- MongoDB for reliable cloud database services
- Flask for lightweight web framework
- Open source community for inspiration

---

<div align="center">

**Built with dedication by [Pranav Rayban](https://www.linkedin.com/in/pranavrayban/)**

⭐ Star this repository if you find it helpful!

</div>
