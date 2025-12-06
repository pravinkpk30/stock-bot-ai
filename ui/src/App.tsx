import { useState } from 'react';
import axios from 'axios';
import './App.css';

const API_BASE_URL = 'http://localhost:8000';

interface AnswerResponse {
  answer: string;
  sources: string[];
}

function App() {
  const [urls, setUrls] = useState<string[]>(['', '', '']);
  const [question, setQuestion] = useState('');
  const [loading, setLoading] = useState(false);
  const [processing, setProcessing] = useState(false);
  const [answer, setAnswer] = useState<AnswerResponse | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [processStatus, setProcessStatus] = useState<string | null>(null);

  const handleUrlChange = (index: number, value: string) => {
    const newUrls = [...urls];
    newUrls[index] = value;
    setUrls(newUrls);
  };

  const handleProcessUrls = async () => {
    setProcessing(true);
    setError(null);
    setProcessStatus(null);
    setAnswer(null);

    try {
      const validUrls = urls.filter(url => url.trim() !== '');
      
      if (validUrls.length === 0) {
        setError('Please enter at least one URL');
        setProcessing(false);
        return;
      }

      const response = await axios.post(`${API_BASE_URL}/process-urls`, {
        urls: validUrls
      });

      setProcessStatus(response.data.message);
    } catch (err: any) {
      setError(err.response?.data?.detail || 'Error processing URLs');
    } finally {
      setProcessing(false);
    }
  };

  const handleAskQuestion = async () => {
    if (!question.trim()) {
      setError('Please enter a question');
      return;
    }

    setLoading(true);
    setError(null);
    setAnswer(null);

    try {
      const response = await axios.post(`${API_BASE_URL}/ask`, {
        question: question
      });

      setAnswer(response.data);
    } catch (err: any) {
      setError(err.response?.data?.detail || 'Error getting answer');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <header className="header">
        <h1>📈 StockBot: News Research Tool</h1>
        <p className="subtitle">AI-powered news analysis with source citations</p>
      </header>

      <div className="container">
        <div className="sidebar">
          <h2>News Article URLs</h2>
          <div className="url-inputs">
            {urls.map((url, index) => (
              <div key={index} className="input-group">
                <label>URL {index + 1}</label>
                <input
                  type="url"
                  value={url}
                  onChange={(e) => handleUrlChange(index, e.target.value)}
                  placeholder={`https://example.com/article${index + 1}`}
                  disabled={processing}
                />
              </div>
            ))}
          </div>

          <button
            className="process-btn"
            onClick={handleProcessUrls}
            disabled={processing}
          >
            {processing ? (
              <>
                <span className="spinner"></span>
                Processing...
              </>
            ) : (
              'Process URLs'
            )}
          </button>

          {processStatus && (
            <div className="success-message">
              ✅ {processStatus}
            </div>
          )}
        </div>

        <div className="main-content">
          <div className="question-section">
            <h2>Ask a Question</h2>
            <div className="input-group">
              <input
                type="text"
                value={question}
                onChange={(e) => setQuestion(e.target.value)}
                placeholder="What would you like to know about the articles?"
                disabled={loading}
                onKeyPress={(e) => {
                  if (e.key === 'Enter' && !loading) {
                    handleAskQuestion();
                  }
                }}
              />
              <button
                className="ask-btn"
                onClick={handleAskQuestion}
                disabled={loading}
              >
                {loading ? (
                  <>
                    <span className="spinner"></span>
                    Thinking...
                  </>
                ) : (
                  'Ask'
                )}
              </button>
            </div>
          </div>

          {error && (
            <div className="error-message">
              ❌ {error}
            </div>
          )}

          {answer && (
            <div className="answer-section">
              <h3>Answer</h3>
              <div className="answer-content">
                {answer.answer}
              </div>

              {answer.sources.length > 0 && (
                <div className="sources-section">
                  <h4>Sources:</h4>
                  <ul className="sources-list">
                    {answer.sources.map((source, index) => (
                      <li key={index}>
                        <a href={source} target="_blank" rel="noopener noreferrer">
                          {source}
                        </a>
                      </li>
                    ))}
                  </ul>
                </div>
              )}
            </div>
          )}

          {!answer && !error && !loading && (
            <div className="placeholder">
              <div className="placeholder-icon">💡</div>
              <p>Process some URLs and ask a question to get started!</p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;
