#!/bin/bash
echo "🚀 Starting Smile Photobooth Application..."
echo "This will start both the Flask backend and React frontend"
echo ""

# Function to cleanup background processes
cleanup() {
    echo ""
    echo "🛑 Shutting down servers..."
    kill $BACKEND_PID 2>/dev/null
    kill $FRONTEND_PID 2>/dev/null
    exit 0
}

# Set up trap to cleanup on exit
trap cleanup SIGINT SIGTERM

# Start backend
echo "📡 Starting Flask backend server on port 5001..."
cd backend
export PATH=$PATH:/home/ubuntu/.local/bin
python3 app.py &
BACKEND_PID=$!
cd ..

# Wait a bit for backend to start
sleep 3

# Start frontend
echo "🎨 Starting React frontend development server..."
cd frontend
npm run dev &
FRONTEND_PID=$!
cd ..

echo ""
echo "✅ Both servers are starting up!"
echo "🔗 Backend API: http://localhost:5001"
echo "🎭 Frontend App: http://localhost:5173"
echo ""
echo "Press Ctrl+C to stop both servers"

# Wait for background processes
wait