# 😄 Smile Photobooth

A fun and intelligent React + Flask web app that auto-captures your smiles and turns them into a photobooth-style selfie strip — complete with an optional custom message and one-click download! 📸✨

---

## 🚀 What It Does

- Uses your **webcam** to detect smiles in real-time
- Automatically captures 3 photos when you're smiling 😁
- Lets you add a cute or clever **message** below the photo strip 💬
- Generates a **vertical photobooth-style collage**
- Allows you to **download** your memory as a single image 📥

---

## 🧠 How It Works

- **Frontend**: React + `react-webcam` + `html2canvas`
- **Backend**: Flask + OpenCV Haarcascade for real-time smile detection

---

## 📸 Demo Flow

1. You smile 😄
2. A picture is auto-snapped 📷
3. Repeat until 3 photos are captured ✨
4. Add a caption (or not, we won’t judge 😎)
5. Preview and download your custom photo strip 🎉

---

## 🛠️ Local Setup

### Backend (Flask + OpenCV)

```bash
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install flask flask-cors opencv-python
python app.py
