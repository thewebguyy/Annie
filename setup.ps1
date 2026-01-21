# Setup Annie - 2026 Scriptwriting OS (PowerShell Version)

Write-Host "🚀 Starting Annie Setup..." -ForegroundColor Cyan

# 1. Backend Setup
Write-Host "Setting up Backend..." -ForegroundColor Yellow
Set-Location server
if (-not (Test-Path venv)) {
    python -m venv venv
}
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
if (-not (Test-Path .env)) {
    Copy-Item .env.example .env
}
Set-Location ..

# 2. Frontend Setup
Write-Host "Installing Frontend Dependencies..." -ForegroundColor Yellow
Set-Location client
npm install
if (-not (Test-Path .env)) {
    Copy-Item .env.example .env
}
Set-Location ..

# 3. Infrastructure
Write-Host "Checking Docker..." -ForegroundColor Yellow
docker-compose up -d

Write-Host "✅ Setup complete! Run 'npm run dev' in /client and 'uvicorn app.main:app' in /server (inside venv)." -ForegroundColor Green
