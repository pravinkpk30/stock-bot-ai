# StockBot Project Structure

## Complete File Tree

```
stock-bot-ai/
│
├── 📁 api/                          # FastAPI Backend
│   ├── main.py                      # API endpoints and business logic
│   ├── requirements.txt             # Python dependencies
│   ├── pyproject.toml              # UV project configuration
│   └── README.md                    # API documentation
│
├── 📁 ui/                           # React Frontend
│   ├── 📁 src/
│   │   ├── App.tsx                  # Main React component
│   │   ├── App.css                  # Application styles
│   │   ├── main.tsx                 # Entry point
│   │   ├── index.css                # Global styles
│   │   └── 📁 assets/               # Static assets
│   ├── index.html                   # HTML template
│   ├── package.json                 # Node dependencies
│   ├── tsconfig.json               # TypeScript config
│   ├── vite.config.ts              # Vite config
│   └── README.md                    # UI documentation
│
├── 📁 streamlit-app/                # Streamlit Prototype (Original)
│   ├── main.py                      # Streamlit application
│   ├── requirements.txt             # Python dependencies
│   ├── pyproject.toml              # UV project configuration
│   ├── uv.lock                     # UV lock file
│   └── README.md                    # Streamlit documentation
│
├── .env                             # Environment variables (GOOGLE_API_KEY)
├── .gitignore                       # Git ignore rules
├── start.sh                         # Quick start script
├── LICENSE                          # License file
└── README.md                        # Main documentation
```

## Component Overview

### 1. API (Backend)

**Technology**: FastAPI + Python 3.11+
**Port**: 8000
**Purpose**: RESTful API for processing URLs and answering questions

**Key Files**:

- `main.py`: Contains all API endpoints and business logic
- `requirements.txt`: Python package dependencies
- `pyproject.toml`: UV configuration for dependency management

**Endpoints**:

- `GET /`: API information
- `GET /health`: Health check
- `POST /process-urls`: Process news articles
- `POST /ask`: Ask questions about articles

### 2. UI (Frontend)

**Technology**: React 18 + TypeScript + Vite
**Port**: 5173
**Purpose**: Modern web interface for the application

**Key Files**:

- `src/App.tsx`: Main application component with all UI logic
- `src/App.css`: Premium dark-themed styling
- `index.html`: HTML template with SEO meta tags

**Features**:

- Responsive design (mobile, tablet, desktop)
- Dark theme with gradients
- Smooth animations
- Real-time loading states
- Error handling

### 3. Streamlit App (Prototype)

**Technology**: Streamlit + Python
**Port**: 8501
**Purpose**: Original prototype application

**Note**: This is the original implementation. The new architecture uses API + UI for better separation of concerns.

## Data Flow

```
User Input (UI)
    ↓
HTTP Request (Axios)
    ↓
FastAPI Backend
    ↓
LangChain Processing
    ↓
Google Gemini AI
    ↓
Response with Sources
    ↓
Display in UI
```

## Setup Order

1. **Environment Setup**

   ```bash
   echo "GOOGLE_API_KEY=your_key" > .env
   ```

2. **Backend Setup**

   ```bash
   cd api
   uv venv
   source .venv/bin/activate
   uv pip install -r requirements.txt
   ```

3. **Frontend Setup**

   ```bash
   cd ui
   npm install
   ```

4. **Run Application**

   ```bash
   # Option 1: Use start script
   ./start.sh

   # Option 2: Manual start
   # Terminal 1:
   cd api && uv run uvicorn main:app --reload

   # Terminal 2:
   cd ui && npm run dev
   ```

## Key Technologies

### Backend

- **FastAPI**: Modern, fast web framework
- **LangChain**: LLM application framework
- **Google Gemini 2.0 Flash**: AI model
- **FAISS**: Vector similarity search
- **HuggingFace**: Text embeddings
- **Pydantic**: Data validation

### Frontend

- **React 18**: UI library
- **TypeScript**: Type safety
- **Vite**: Build tool
- **Axios**: HTTP client
- **CSS3**: Modern styling

## Environment Variables

Required in `.env` file:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

## Ports

- **API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs
- **UI**: http://localhost:5173
- **Streamlit**: http://localhost:8501

## Development Workflow

1. Make changes to code
2. Backend auto-reloads (with `--reload` flag)
3. Frontend auto-reloads (Vite HMR)
4. Test in browser
5. Commit changes

## Production Deployment

### Backend

- Deploy to: AWS Lambda, Google Cloud Run, Heroku, or Docker
- Use production ASGI server (Uvicorn with workers)

### Frontend

- Build: `npm run build`
- Deploy `dist/` to: Vercel, Netlify, AWS S3, or any static host

## Notes

- The `streamlit-app` folder contains the original prototype
- The new architecture (API + UI) is the recommended approach
- Both implementations share the same core logic
- The UI provides a better user experience and is production-ready
