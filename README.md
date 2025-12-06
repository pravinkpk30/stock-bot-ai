# StockBot: AI-Powered News Research Tool 📈

A full-stack application that uses AI to analyze news articles and answer questions with source citations. Built with FastAPI backend, React frontend, and Google's Gemini AI.

## 🌟 Features

- **URL Processing**: Load and analyze multiple news article URLs
- **AI-Powered Q&A**: Ask questions and get intelligent answers using Google Gemini 2.0 Flash
- **Source Citations**: Get transparent answers with source references
- **Vector Search**: Uses FAISS for efficient semantic search
- **Modern UI**: Beautiful, responsive React interface with dark theme
- **RESTful API**: Well-documented FastAPI backend

## 📁 Project Structure

```
stock-bot-ai/
├── api/                    # FastAPI Backend
│   ├── main.py            # API endpoints and logic
│   ├── requirements.txt   # Python dependencies
│   └── README.md          # API documentation
│
├── ui/                     # React Frontend
│   ├── src/
│   │   ├── App.tsx        # Main React component
│   │   ├── App.css        # Styling
│   │   └── main.tsx       # Entry point
│   ├── package.json       # Node dependencies
│   └── README.md          # UI documentation
│
├── streamlit-app/         # Streamlit Prototype (Original)
│   ├── main.py           # Streamlit application
│   ├── requirements.txt  # Python dependencies
│   └── README.md         # Streamlit documentation
│
├── .env                   # Environment variables
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

## 🚀 Quick Start

### Prerequisites

- **Python 3.11+**
- **Node.js 20+**
- **uv** (Python package manager)
- **Google API Key** ([Get one here](https://makersuite.google.com/app/apikey))

### 1. Clone and Setup Environment

```bash
cd stock-bot-ai

# Create .env file in the root directory
echo "GOOGLE_API_KEY=your_google_api_key_here" > .env
```

### 2. Start the Backend API

```bash
cd api

# Create virtual environment
uv venv

# Activate virtual environment
source .venv/bin/activate  # macOS/Linux
# or
.venv\Scripts\activate     # Windows

# Install dependencies
uv pip install -r requirements.txt

# Run the API
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

- Swagger docs: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### 3. Start the Frontend UI

Open a new terminal:

```bash
cd ui

# Install dependencies
npm install

# Run the development server
npm run dev
```

The UI will be available at `http://localhost:5173`

## 🎯 How to Use

1. **Open the UI** at `http://localhost:5173`
2. **Enter URLs**: Add up to 3 news article URLs in the sidebar
3. **Process URLs**: Click "Process URLs" to analyze the articles
4. **Ask Questions**: Enter your question in the main area
5. **Get Answers**: View AI-generated answers with source citations

## 🛠️ Technology Stack

### Backend

- **FastAPI**: Modern Python web framework
- **LangChain**: LLM application framework
- **Google Gemini 2.0 Flash**: Large language model
- **FAISS**: Vector similarity search
- **HuggingFace Embeddings**: Text embeddings
- **Uvicorn**: ASGI server

### Frontend

- **React 18**: UI library
- **TypeScript**: Type-safe JavaScript
- **Vite**: Fast build tool
- **Axios**: HTTP client
- **CSS3**: Modern styling

### Streamlit App (Prototype)

- **Streamlit**: Quick prototyping framework
- Same backend technologies as API

## 📚 API Endpoints

### `GET /`

Root endpoint with API information

### `GET /health`

Health check endpoint

### `POST /process-urls`

Process news article URLs

**Request:**

```json
{
  "urls": ["https://example.com/article1", "https://example.com/article2"]
}
```

**Response:**

```json
{
  "status": "success",
  "message": "URLs processed successfully",
  "urls_processed": 2
}
```

### `POST /ask`

Ask questions about processed articles

**Request:**

```json
{
  "question": "What is the main topic?"
}
```

**Response:**

```json
{
  "answer": "The main topic is...",
  "sources": ["https://example.com/article1"]
}
```

## 🔧 Development

### Backend Development

```bash
cd api
source .venv/bin/activate
uvicorn main:app --reload
```

### Frontend Development

```bash
cd ui
npm run dev
```

### Streamlit Development

```bash
cd streamlit-app
uv run streamlit run main.py
```

## 📦 Building for Production

### Backend

The FastAPI backend can be deployed using:

- Docker
- Heroku
- AWS Lambda
- Google Cloud Run

### Frontend

```bash
cd ui
npm run build
```

Deploy the `dist/` folder to:

- Vercel
- Netlify
- AWS S3 + CloudFront
- Any static hosting service

## 🐛 Troubleshooting

### Backend Issues

**Issue**: `ModuleNotFoundError`

```bash
cd api
uv pip install -r requirements.txt
```

**Issue**: API not accessible

- Check if port 8000 is available
- Ensure CORS is configured correctly

### Frontend Issues

**Issue**: API connection failed

- Ensure backend is running at `http://localhost:8000`
- Check browser console for CORS errors

**Issue**: Build errors

```bash
cd ui
rm -rf node_modules package-lock.json
npm install
```

## 🔐 Environment Variables

Create a `.env` file in the root directory:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

## 📝 License

This project is licensed under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Support

For issues and questions, please open an issue on GitHub.

---

**Note**: This application requires an active internet connection to fetch articles and communicate with the Google Gemini API.
