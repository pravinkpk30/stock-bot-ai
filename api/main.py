import os
import pickle
from typing import List, Optional
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, HttpUrl
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="StockBot API", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],  # React dev servers
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    api_key=os.getenv("GOOGLE_API_KEY")
)

# File path for FAISS storage
FAISS_STORE_PATH = "faiss_store.pkl"


# Pydantic models
class URLRequest(BaseModel):
    urls: List[HttpUrl]


class QuestionRequest(BaseModel):
    question: str


class ProcessResponse(BaseModel):
    status: str
    message: str
    urls_processed: int


class AnswerResponse(BaseModel):
    answer: str
    sources: List[str]


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "StockBot API is running",
        "version": "1.0.0",
        "endpoints": {
            "POST /process-urls": "Process news article URLs",
            "POST /ask": "Ask questions about processed articles",
            "GET /health": "Health check"
        }
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}


@app.post("/process-urls", response_model=ProcessResponse)
async def process_urls(request: URLRequest):
    """
    Process news article URLs and create embeddings
    """
    try:
        # Convert HttpUrl objects to strings
        urls = [str(url) for url in request.urls]
        
        if not urls or all(url == "" for url in urls):
            raise HTTPException(status_code=400, detail="No valid URLs provided")
        
        # Filter out empty URLs
        valid_urls = [url for url in urls if url.strip()]
        
        # Load data from URLs
        loader = UnstructuredURLLoader(urls=valid_urls)
        data = loader.load()
        
        # Split text into chunks
        text_splitter = RecursiveCharacterTextSplitter(
            separators=['\n\n', '\n', '.', ','],
            chunk_size=1000
        )
        docs = text_splitter.split_documents(data)
        
        # Create embeddings
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2",
            model_kwargs={'device': 'cpu'},
            encode_kwargs={'normalize_embeddings': True}
        )
        
        # Create FAISS vector store
        vectorstore = FAISS.from_documents(docs, embeddings)
        
        # Save to pickle file
        with open(FAISS_STORE_PATH, "wb") as f:
            pickle.dump(vectorstore, f)
        
        return ProcessResponse(
            status="success",
            message="URLs processed successfully",
            urls_processed=len(valid_urls)
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing URLs: {str(e)}")


@app.post("/ask", response_model=AnswerResponse)
async def ask_question(request: QuestionRequest):
    """
    Ask a question about the processed articles
    """
    try:
        if not os.path.exists(FAISS_STORE_PATH):
            raise HTTPException(
                status_code=400,
                detail="No processed data found. Please process URLs first."
            )
        
        # Load the vector store
        with open(FAISS_STORE_PATH, "rb") as f:
            vectorstore = pickle.load(f)
        
        # Retrieve relevant documents
        retriever = vectorstore.as_retriever()
        docs = retriever.invoke(request.question)
        
        # Prepare context from retrieved documents
        context = "\n\n".join([doc.page_content for doc in docs])
        sources = list(set([
            doc.metadata.get('source', '')
            for doc in docs
            if doc.metadata.get('source')
        ]))
        
        # Create prompt and get answer from LLM
        prompt = f"""Based on the following context, answer the question.
        
Context:
{context}

Question: {request.question}

Answer:"""
        
        answer = llm.invoke(prompt)
        
        return AnswerResponse(
            answer=answer.content,
            sources=sources
        )
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error answering question: {str(e)}")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
