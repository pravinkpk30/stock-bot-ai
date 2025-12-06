# 🚀 Quick Reference Guide

## One-Command Start

```bash
./start.sh
```

## Manual Commands

### Backend

```bash
cd api
source .venv/bin/activate
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend

```bash
cd ui
npm run dev
```

### Streamlit (Original)

```bash
cd streamlit-app
uv run streamlit run main.py
```

## URLs

| Service     | URL                         | Description      |
| ----------- | --------------------------- | ---------------- |
| Frontend    | http://localhost:5173       | React UI         |
| Backend API | http://localhost:8000       | FastAPI Server   |
| API Docs    | http://localhost:8000/docs  | Swagger UI       |
| API ReDoc   | http://localhost:8000/redoc | Alternative Docs |
| Streamlit   | http://localhost:8501       | Original App     |

## API Endpoints

### Process URLs

```bash
curl -X POST http://localhost:8000/process-urls \
  -H "Content-Type: application/json" \
  -d '{"urls": ["https://example.com/article"]}'
```

### Ask Question

```bash
curl -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "What is the main topic?"}'
```

### Health Check

```bash
curl http://localhost:8000/health
```

## Project Structure

```
stock-bot-ai/
├── api/              # FastAPI Backend
├── ui/               # React Frontend
├── streamlit-app/    # Original Streamlit App
├── .env             # Environment Variables
└── start.sh         # Quick Start Script
```

## Environment Setup

```bash
# Create .env file
echo "GOOGLE_API_KEY=your_key_here" > .env
```

## Installation

### Backend

```bash
cd api
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

### Frontend

```bash
cd ui
npm install
```

## Common Issues

### Port Already in Use

```bash
# Kill process on port 8000
lsof -ti:8000 | xargs kill -9

# Kill process on port 5173
lsof -ti:5173 | xargs kill -9
```

### Module Not Found

```bash
# Backend
cd api
uv pip install -r requirements.txt

# Frontend
cd ui
rm -rf node_modules package-lock.json
npm install
```

### CORS Error

- Ensure backend is running on port 8000
- Check CORS settings in `api/main.py`

## Development Tips

### Hot Reload

- Backend: Auto-reloads with `--reload` flag
- Frontend: Auto-reloads with Vite HMR

### Debugging

- Backend: Check terminal for errors
- Frontend: Check browser console (F12)
- API: Use `/docs` endpoint to test

### Testing API

1. Go to http://localhost:8000/docs
2. Try out endpoints interactively
3. View request/response examples

## File Locations

### Backend Code

- Main API: `api/main.py`
- Dependencies: `api/requirements.txt`

### Frontend Code

- Main Component: `ui/src/App.tsx`
- Styles: `ui/src/App.css`
- HTML: `ui/index.html`

### Documentation

- Main: `README.md`
- Structure: `PROJECT_STRUCTURE.md`
- Summary: `IMPLEMENTATION_SUMMARY.md`

## Build for Production

### Backend

```bash
cd api
uv pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
```

### Frontend

```bash
cd ui
npm run build
# Deploy dist/ folder
```

## Git Commands

```bash
# Add all changes
git add .

# Commit
git commit -m "Your message"

# Push
git push origin main
```

## Useful Commands

### Check Python Version

```bash
python --version  # Should be 3.11+
```

### Check Node Version

```bash
node --version    # Should be 20+
```

### Check if Services are Running

```bash
# Check port 8000 (API)
lsof -i:8000

# Check port 5173 (UI)
lsof -i:5173
```

### View Logs

```bash
# Backend logs are in terminal
# Frontend logs are in browser console
```

## Support

- 📚 Read: `README.md`
- 🏗️ Structure: `PROJECT_STRUCTURE.md`
- ✨ Summary: `IMPLEMENTATION_SUMMARY.md`
- 🔧 API Docs: http://localhost:8000/docs

---

**Quick Start**: `./start.sh` → Open http://localhost:5173 🚀
