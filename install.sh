#!/bin/bash
# Installation Script for Tariff Management Playwright Tests
# Run this script to set up everything

echo "╔══════════════════════════════════════════════════════════════╗"
echo "║   TARIFF MANAGEMENT - INSTALLATION SCRIPT                    ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""

# Step 1: Install system dependencies
echo "📦 Step 1: Installing system dependencies..."
echo "Please run these commands manually (requires sudo):"
echo ""
echo "sudo apt update"
echo "sudo apt install -y python3-pip python3-venv python3-full"
echo ""
read -p "Press Enter after running the above commands..."

# Step 2: Create virtual environment
echo ""
echo "🔧 Step 2: Creating virtual environment..."
python3 -m venv venv

# Step 3: Activate virtual environment
echo ""
echo "✅ Step 3: Activating virtual environment..."
source venv/bin/activate

# Step 4: Upgrade pip
echo ""
echo "⬆️  Step 4: Upgrading pip..."
pip install --upgrade pip

# Step 5: Install Python packages
echo ""
echo "📦 Step 5: Installing Python packages..."
pip install -r requirements.txt

# Step 6: Install Playwright browsers
echo ""
echo "🌐 Step 6: Installing Playwright browsers..."
playwright install chromium

# Step 7: Verify installation
echo ""
echo "✔️  Step 7: Verifying installation..."
echo ""
echo "Python version:"
python --version
echo ""
echo "Pip version:"
pip --version
echo ""
echo "Pytest version:"
pytest --version
echo ""
echo "Playwright version:"
playwright --version

echo ""
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║   ✅ INSTALLATION COMPLETE!                                  ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""
echo "📝 Next Steps:"
echo "1. Activate virtual environment: source venv/bin/activate"
echo "2. Run tests: pytest --headed --slowmo=1000 -v"
echo "3. Check results in assets/ and reports/ folders"
echo ""
echo "🎉 Happy Testing!"
