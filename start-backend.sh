#!/bin/bash
echo "Starting Flask backend server..."
cd backend
export PATH=$PATH:/home/ubuntu/.local/bin
python3 app.py