# Real-time AI Meeting Assistant - Windows Setup Script

Write-Host "🚀 Setting up Real-time AI Meeting Assistant..." -ForegroundColor Cyan
Write-Host ""

# Create virtual environment if it doesn't exist
if (-not (Test-Path "venv")) {
    Write-Host "📦 Creating virtual environment..." -ForegroundColor Yellow
    python -m venv venv
    Write-Host "✓ Virtual environment created" -ForegroundColor Green
} else {
    Write-Host "✓ Virtual environment already exists" -ForegroundColor Green
}

# Activate virtual environment
Write-Host ""
Write-Host "📦 Activating virtual environment..." -ForegroundColor Yellow
& ".\venv\Scripts\Activate.ps1"

Write-Host "✓ Virtual environment activated" -ForegroundColor Green

# Upgrade pip
Write-Host ""
Write-Host "📦 Upgrading pip..." -ForegroundColor Yellow
python -m pip install --upgrade pip --quiet
Write-Host "✓ Pip upgraded" -ForegroundColor Green

Write-Host ""
Write-Host "✅ Setup complete!" -ForegroundColor Green
Write-Host ""
Write-Host "Note: Some packages in requirements.txt require LiveKit setup." -ForegroundColor Yellow
Write-Host "The demo works without them using mock implementations." -ForegroundColor Yellow
Write-Host ""
Write-Host "To run the demo:" -ForegroundColor Cyan
Write-Host "  .\venv\Scripts\Activate.ps1" -ForegroundColor White
Write-Host "  `$env:PYTHONIOENCODING='utf-8'; python demo.py" -ForegroundColor White
Write-Host ""

