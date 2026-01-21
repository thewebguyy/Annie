#!/bin/bash

# Setup Annie - 2026 Scriptwriting OS

echo "🚀 Starting Annie Setup..."

# 1. Backend Setup
echo "Creating Python Virtual Environment..."
cd server
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
cd ..

# 2. Frontend Setup
echo "Installing Frontend Dependencies..."
cd client
npm install
cp .env.example .env
cd ..

# 3. Infrastructure
echo "Checking Docker..."
docker-compose up -d

echo "✅ Setup complete! Run 'npm run dev' in /client and 'uvicorn app.main:app' in /server."
