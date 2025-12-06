#!/bin/bash

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}🚀 Starting StockBot Application${NC}\n"

# Check if .env file exists
if [ ! -f .env ]; then
    echo -e "${RED}❌ Error: .env file not found${NC}"
    echo -e "Please create a .env file with your GOOGLE_API_KEY"
    echo -e "Example: echo 'GOOGLE_API_KEY=your_key_here' > .env"
    exit 1
fi

# Start API in background
echo -e "${GREEN}📡 Starting Backend API...${NC}"
cd api
source .venv/bin/activate 2>/dev/null || true
uvicorn main:app --reload --host 0.0.0.0 --port 8000 &
API_PID=$!
cd ..

# Wait for API to start
echo -e "${BLUE}⏳ Waiting for API to start...${NC}"
sleep 3

# Start UI
echo -e "${GREEN}🎨 Starting Frontend UI...${NC}"
cd ui
npm run dev &
UI_PID=$!
cd ..

echo -e "\n${GREEN}✅ Application started successfully!${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "📡 API: http://localhost:8000"
echo -e "📚 API Docs: http://localhost:8000/docs"
echo -e "🎨 UI: http://localhost:5173"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "\nPress Ctrl+C to stop all services\n"

# Function to cleanup on exit
cleanup() {
    echo -e "\n${RED}🛑 Stopping services...${NC}"
    kill $API_PID 2>/dev/null
    kill $UI_PID 2>/dev/null
    exit 0
}

# Trap Ctrl+C
trap cleanup INT

# Wait for processes
wait
