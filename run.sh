#!/bin/bash
# run.sh – Bootstrap HOOK Travel Dev Environment

echo "🚀 HOOK Travel – Itinerary Generator CLI"
echo "----------------------------------------"

# Step 1: Create virtual environment if missing
if [ ! -d "venv" ]; then
  echo "📦 Creating Python virtual environment..."
  python3 -m venv venv
fi
source venv/bin/activate

# Step 2: Install dependencies
echo "📚 Installing dependencies..."
pip install -r requirements.txt

# Step 3: Run Itinerary Generator
echo "🧭 Generating sample itinerary PDF..."
python index.py

# Step 4: Done
echo "✅ Output saved to hook_trip_preview.pdf"
