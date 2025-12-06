# StockBot: News Research Tool 📈

A Streamlit-based AI application that allows users to analyze news articles using Google's Gemini AI and retrieval-augmented generation (RAG) techniques. The app processes news article URLs, creates embeddings, and answers questions based on the content.

## Features

- 📰 **URL Processing**: Load and process up to 3 news article URLs simultaneously
- 🤖 **AI-Powered Q&A**: Ask questions about the articles and get intelligent answers using Google's Gemini 2.0 Flash model
- 🔍 **Source Citations**: Get answers with source references for transparency
- 💾 **Vector Storage**: Uses FAISS for efficient similarity search and retrieval
- 🧠 **Semantic Search**: Leverages HuggingFace embeddings for accurate document retrieval

## Technology Stack

- **Frontend**: Streamlit
- **LLM**: Google Gemini 2.0 Flash (via `langchain-google-genai`)
- **Embeddings**: HuggingFace Sentence Transformers (`all-MiniLM-L6-v2`)
- **Vector Store**: FAISS (Facebook AI Similarity Search)
- **Document Processing**: LangChain Community (UnstructuredURLLoader)
- **Text Splitting**: LangChain Text Splitters (RecursiveCharacterTextSplitter)

## Prerequisites

Before running the application, ensure you have the following installed:

1. **Python 3.11+**: The application requires Python 3.11 or higher
2. **uv**: A fast Python package installer and resolver
   ```bash
   # Install uv (if not already installed)
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```
3. **Google API Key**: You need a Google API key to use the Gemini model
   - Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

## Installation

### 1. Clone the Repository

```bash
cd /path/to/stock-bot-ai/streamlit-app
```

### 2. Create Virtual Environment

Using `uv`, create a virtual environment:

```bash
uv venv
```

### 3. Activate Virtual Environment

**On macOS/Linux:**

```bash
source .venv/bin/activate
```

**On Windows:**

```bash
.venv\Scripts\activate
```

### 4. Install Dependencies

Install all required packages using `uv`:

```bash
uv pip install -r requirements.txt
```

### 5. Set Up Environment Variables

Create a `.env` file in the `streamlit-app` directory and add your Google API key:

```bash
GOOGLE_API_KEY=your_google_api_key_here
```

## Usage

### Running the Application

#### Option 1: Using `uv run` (Recommended)

This method automatically uses the virtual environment without manual activation:

```bash
uv run streamlit run main.py
```

#### Option 2: Traditional Method

After activating the virtual environment:

```bash
streamlit run main.py
```

### Accessing the Application

Once the application starts, you'll see output like:

```
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.x.x:8501
```

Open your browser and navigate to `http://localhost:8501`

## How to Use the App

1. **Enter URLs**: In the sidebar, enter up to 3 news article URLs
2. **Process URLs**: Click the "Process URLs" button to load and embed the articles
3. **Wait for Processing**: The app will:
   - Load the data from URLs
   - Split the text into chunks
   - Create embeddings using HuggingFace models
   - Store the embeddings in a FAISS index
4. **Ask Questions**: Once processing is complete, enter your question in the text input
5. **Get Answers**: The app will retrieve relevant information and generate an answer with sources

## Project Structure

```
streamlit-app/
├── main.py                 # Main Streamlit application
├── requirements.txt        # Python dependencies
├── pyproject.toml         # Project configuration
├── .env                   # Environment variables (create this)
├── .venv/                 # Virtual environment (created by uv)
├── faiss_store_openai.pkl # FAISS index storage (created after processing URLs)
└── README.md              # This file
```

## How It Works

### 1. Document Loading

The app uses `UnstructuredURLLoader` to fetch and parse content from the provided URLs.

### 2. Text Splitting

Content is split into manageable chunks using `RecursiveCharacterTextSplitter`:

- Chunk size: 1000 characters
- Separators: `\n\n`, `\n`, `.`, `,`

### 3. Embedding Generation

Text chunks are converted to vector embeddings using HuggingFace's `all-MiniLM-L6-v2` model:

- Device: CPU
- Normalized embeddings for better similarity search

### 4. Vector Storage

Embeddings are stored in a FAISS index for efficient similarity search and persisted to disk as `faiss_store_openai.pkl`.

### 5. Question Answering

When a question is asked:

1. The question is used to retrieve relevant document chunks from FAISS
2. Retrieved chunks are combined into context
3. A prompt is created with the context and question
4. Google's Gemini 2.0 Flash model generates an answer
5. Sources are extracted and displayed

## Dependencies

```
langchain-google-genai     # Google Gemini integration
langchain-community        # Document loaders and vector stores
langchain                  # Core LangChain functionality
langchain-text-splitters   # Text splitting utilities
streamlit                  # Web application framework
faiss-cpu                  # Vector similarity search
unstructured               # Document parsing
python-dotenv              # Environment variable management
sentence-transformers      # HuggingFace embeddings
```

## Troubleshooting

### Issue: `ModuleNotFoundError: No module named 'langchain.chains'`

**Solution**: Make sure you've installed all dependencies using `uv pip install -r requirements.txt`

### Issue: `AttributeError: 'VectorStoreRetriever' object has no attribute 'get_relevant_documents'`

**Solution**: This has been fixed in the latest version. Use `retriever.invoke(query)` instead.

### Issue: Streamlit command not found

**Solution**: Ensure your virtual environment is activated or use `uv run streamlit run main.py`

### Issue: API Key Error

**Solution**: Make sure your `.env` file contains a valid `GOOGLE_API_KEY`

## Performance Optimization

For better performance, consider installing the Watchdog module:

```bash
# On macOS
xcode-select --install
uv pip install watchdog
```

## Future Enhancements

- [ ] Support for more than 3 URLs
- [ ] PDF document support
- [ ] Chat history and conversation memory
- [ ] Multiple embedding model options
- [ ] Export answers to PDF/Markdown
- [ ] Batch processing of multiple questions

## License

This project is part of the stock-bot-ai application.

## Contributing

Feel free to submit issues and enhancement requests!

---

**Note**: This application requires an active internet connection to fetch articles and communicate with the Google Gemini API.
