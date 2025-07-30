#!/usr/bin/env python3
"""
Simple test script for the Flask backend
"""
import requests
import json
import base64
import time
import subprocess
import sys
import os

def test_backend():
    print("🧪 Testing Smile Photobooth Backend")
    print("=" * 40)
    
    # Test health endpoint
    try:
        print("📡 Testing health endpoint...")
        response = requests.get('http://localhost:5001/health', timeout=5)
        if response.status_code == 200:
            print("✅ Health endpoint working!")
            print(f"   Response: {response.json()}")
        else:
            print(f"❌ Health endpoint failed: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Could not connect to backend: {e}")
        print("   Make sure the Flask server is running on port 5001")
        return False
    
    print("\n🎯 Testing smile detection endpoint...")
    # Create a simple test image (1x1 pixel base64 encoded)
    test_image = "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEAYABgAAD/2wBDAAEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQH/2wBDAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQH/wAARCAABAAEDASIAAhEBAxEB/8QAFQABAQAAAAAAAAAAAAAAAAAAAAv/xAAUEAEAAAAAAAAAAAAAAAAAAAAA/8QAFQEBAQAAAAAAAAAAAAAAAAAAAAX/xAAUEQEAAAAAAAAAAAAAAAAAAAAA/9oADAMBAAIRAxEAPwA/8A"
    
    try:
        response = requests.post(
            'http://localhost:5001/predict',
            json={'image': test_image},
            headers={'Content-Type': 'application/json'},
            timeout=10
        )
        
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Smile detection endpoint working!")
            print(f"   Response: {result}")
            return True
        else:
            print(f"❌ Smile detection failed: {response.status_code}")
            print(f"   Response: {response.text}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Error testing smile detection: {e}")
        return False

if __name__ == "__main__":
    success = test_backend()
    if success:
        print("\n🎉 Backend tests passed!")
        sys.exit(0)
    else:
        print("\n💥 Backend tests failed!")
        sys.exit(1)