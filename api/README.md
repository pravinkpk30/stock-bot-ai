# API Backend

FastAPI backend for StockBot News Research Tool.

## Setup

1. Create virtual environment:

```bash
uv venv
```

2. Activate virtual environment:

```bash
source .venv/bin/activate  # macOS/Linux
# or
.venv\Scripts\activate  # Windows
```

3. Install dependencies:

```bash
uv pip install -r requirements.txt
```

4. Create `.env` file in the root directory with:

```
GOOGLE_API_KEY=your_google_api_key_here
```

## Running the API

### Method 1: With activated virtual environment (Recommended)

```bash
# Activate virtual environment
source .venv/bin/activate  # macOS/Linux
# or
.venv\Scripts\activate  # Windows

# Run the API
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Method 2: One-line command

```bash
source .venv/bin/activate && uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

## API Documentation

Once running, visit:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Endpoints

### `GET /`

Root endpoint with API information

### `GET /health`

Health check endpoint

### `POST /process-urls`

Process news article URLs and create embeddings

**Request Body:**

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

**Request Body:**

```json
{
  "question": "What is the main topic of the articles?"
}
```

**Response:**

```json
{
  "answer": "The main topic is...",
  "sources": ["https://example.com/article1", "https://example.com/article2"]
}
```
