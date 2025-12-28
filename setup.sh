#!/bin/bash

echo "🚀 Setting up Real-time AI Meeting Assistant..."

if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

source venv/bin/activate
echo "✓ Virtual environment activated"

echo "📦 Upgrading pip..."
pip install --upgrade pip

echo "📦 Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Set your API keys:"
echo "   export OPENAI_API_KEY='your-openai-key'"
echo ""
echo "2. Run the demo:"
echo "   python demo.py"
