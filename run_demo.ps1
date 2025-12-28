# Quick script to run the demo

# Activate virtual environment
if (Test-Path "venv\Scripts\Activate.ps1") {
    & ".\venv\Scripts\Activate.ps1"
} else {
    Write-Host "⚠ Virtual environment not found. Run setup.ps1 first." -ForegroundColor Yellow
    exit 1
}

# Set encoding for Windows
$env:PYTHONIOENCODING = "utf-8"

# Run the demo
python demo.py

