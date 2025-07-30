# 🚀 Smile Photobooth - Setup & Installation Guide

This guide will help you set up and run the Smile Photobooth application with both frontend and backend components.

## 📋 Prerequisites

- **Python 3.7+** (for backend)
- **Node.js 16+** and **npm** (for frontend)
- **Webcam access** (for smile detection)

## 🛠️ Installation

### 1. Backend Setup (Flask + OpenCV)

```bash
# Navigate to backend directory
cd backend

# Install Python dependencies
pip install -r requirements.txt
# OR if you get externally-managed-environment error:
pip install -r requirements.txt --break-system-packages
```

### 2. Frontend Setup (React + Vite)

```bash
# Navigate to frontend directory
cd frontend

# Install Node.js dependencies
npm install
```

## 🏃‍♂️ Running the Application

### Option 1: Run Both Services Together (Recommended)

```bash
# From the project root directory
chmod +x start-both.sh
./start-both.sh
```

This will start:
- **Backend API** on `http://localhost:5001`
- **Frontend App** on `http://localhost:5173`

### Option 2: Run Services Separately

#### Start Backend
```bash
# From project root
chmod +x start-backend.sh
./start-backend.sh

# OR manually:
cd backend
python3 app.py
```

#### Start Frontend
```bash
# From project root  
chmod +x start-frontend.sh
./start-frontend.sh

# OR manually:
cd frontend
npm run dev
```

## 🧪 Testing the Setup

### Test Backend Only
```bash
cd backend
python3 test_backend.py
```

### Test Full Application
1. Open your browser to `http://localhost:5173`
2. You should see the Smile Photobooth interface
3. Check the "Backend Connected" status indicator
4. Click "Start Photobooth" to begin

## 🔧 Troubleshooting

### Backend Issues

**"Cannot connect to backend server"**
- Make sure Flask server is running on port 5001
- Check that all Python dependencies are installed
- Verify OpenCV is working: `python3 -c "import cv2; print('OpenCV OK')"`

**"Port already in use"**
- Change the port in `backend/app.py` (line with `port=5001`)
- Update the frontend API calls in `frontend/src/App.jsx` to match

**"OpenCV/Haar cascade errors"**
- Ensure opencv-python is properly installed
- Test: `python3 -c "import cv2; print(cv2.data.haarcascades)"`

### Frontend Issues

**"npm install fails"**
```bash
# Clear npm cache and retry
npm cache clean --force
npm install
```

**"Development server won't start"**
```bash
# Check if port 5173 is available
lsof -i :5173
# Kill any processes using the port, then restart
```

### Webcam Issues

**"Could not access webcam"**
- Grant webcam permissions in your browser
- Make sure no other applications are using the webcam
- Try refreshing the page after granting permissions

## 🎯 Application Features

- **Auto Smile Detection**: Uses OpenCV Haar cascades for real-time smile detection
- **Manual Capture Fallback**: If backend is disconnected, use manual capture mode
- **Photo Strip Generation**: Creates a vintage photobooth-style vertical strip
- **Custom Messages**: Add personalized text to your photo strip
- **One-Click Download**: Save your photo strip as a JPEG file

## 🏗️ Architecture

```
📁 Smile Photobooth
├── 📁 backend/          # Flask API server
│   ├── app.py          # Main Flask application
│   ├── requirements.txt # Python dependencies
│   └── test_backend.py # Backend testing script
├── 📁 frontend/         # React web application  
│   ├── src/
│   │   ├── App.jsx     # Main React component
│   │   └── ...
│   ├── package.json    # Node.js dependencies
│   └── ...
├── start-both.sh       # Start both services
├── start-backend.sh    # Start only backend
├── start-frontend.sh   # Start only frontend
└── README.md          # Project overview
```

## 🔌 API Endpoints

- **GET** `/health` - Backend health check
- **POST** `/predict` - Smile detection endpoint
  ```json
  {
    "image": "data:image/jpeg;base64,..."
  }
  ```

## 🎨 Tech Stack

| Component | Technology |
|-----------|------------|
| Frontend | React 19, Vite, TailwindCSS |
| Backend | Flask, OpenCV, NumPy |
| Image Processing | HTML5 Canvas, html2canvas |
| Webcam | getUserMedia API, react-webcam |

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test both frontend and backend
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

---

**Happy Smiling! 😄📸**