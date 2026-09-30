# 🚀 INSTALLATION GUIDE - Step by Step

## System Requirements
- Ubuntu/Debian Linux
- Python 3.8 or higher (✅ You have Python 3.14.4)
- sudo access for system packages

---

## 📋 MANUAL INSTALLATION STEPS

### Step 1: Install System Dependencies

Run these commands in your terminal:

```bash
sudo apt update
sudo apt install -y python3-pip python3-venv python3-full
```

**What this does:**
- `python3-pip` - Python package installer
- `python3-venv` - Virtual environment support
- `python3-full` - Full Python installation

---

### Step 2: Create Virtual Environment

```bash
cd /home/selvaganesh/Selva-Backup/Git/Playwright/Tariff_Management
python3 -m venv venv
```

**What this does:**
- Creates isolated Python environment in `venv/` folder
- Keeps project dependencies separate from system Python

---

### Step 3: Activate Virtual Environment

```bash
source venv/bin/activate
```

**You'll see:**
- `(venv)` prefix in your terminal prompt
- Means virtual environment is active

---

### Step 4: Upgrade pip

```bash
pip install --upgrade pip
```

**What this does:**
- Ensures you have latest pip version

---

### Step 5: Install Python Packages

```bash
pip install -r requirements.txt
```

**This installs:**
- playwright==1.42.0
- pytest==8.1.1
- pytest-playwright==0.4.4
- pytest-html==4.1.1
- Pillow==10.2.0
- python-docx==1.1.0

---

### Step 6: Install Playwright Browsers

```bash
playwright install chromium
```

**What this does:**
- Downloads Chromium browser for testing
- Takes ~100-200MB

---

### Step 7: Verify Installation

```bash
# Check Python
python --version

# Check pip
pip --version

# Check pytest
pytest --version

# Check playwright
playwright --version
```

**Expected output:**
```
Python 3.14.4
pip 24.x.x
pytest 8.1.1
Playwright 1.42.0
```

---

## ✅ QUICK INSTALLATION (Copy-Paste All)

```bash
# Install system dependencies (requires sudo)
sudo apt update && sudo apt install -y python3-pip python3-venv python3-full

# Navigate to project
cd /home/selvaganesh/Selva-Backup/Git/Playwright/Tariff_Management

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install Python packages
pip install --upgrade pip
pip install -r requirements.txt

# Install Playwright browsers
playwright install chromium

# Verify installation
python --version && pip --version && pytest --version && playwright --version
```

---

## 🎯 AFTER INSTALLATION - Run Tests

### Every time you want to run tests:

```bash
# 1. Navigate to project
cd /home/selvaganesh/Selva-Backup/Git/Playwright/Tariff_Management

# 2. Activate virtual environment
source venv/bin/activate

# 3. Run tests
pytest --headed --slowmo=1000 -v
```

---

## 🔄 ALTERNATIVE: Using install.sh Script

We've created an automated script for you:

```bash
cd /home/selvaganesh/Selva-Backup/Git/Playwright/Tariff_Management
./install.sh
```

**Note:** You'll still need to run the sudo commands manually when prompted.

---

## 🐛 Troubleshooting

### Issue: "command not found: pip"
**Solution:** Install python3-pip:
```bash
sudo apt install python3-pip
```

### Issue: "No module named 'venv'"
**Solution:** Install python3-venv:
```bash
sudo apt install python3-venv
```

### Issue: "playwright: command not found"
**Solution:** Make sure virtual environment is activated:
```bash
source venv/bin/activate
pip install playwright
```

### Issue: Virtual environment activation doesn't work
**Solution:** Check if venv exists:
```bash
ls -la venv/
# If not, create it:
python3 -m venv venv
```

---

## 📁 What Gets Installed Where

```
Tariff_Management/
├── venv/                    ← Virtual environment (new)
│   ├── bin/                 ← Python, pip, pytest executables
│   ├── lib/                 ← Installed packages
│   └── include/             ← Python headers
├── tests/                   ← Your test files
├── assets/                  ← Screenshot folders
├── docs/                    ← Documentation
└── requirements.txt         ← Package list
```

---

## 💡 Important Notes

1. **Always activate virtual environment** before running tests:
   ```bash
   source venv/bin/activate
   ```

2. **To deactivate** virtual environment:
   ```bash
   deactivate
   ```

3. **Virtual environment is local** - only affects this project

4. **Don't commit venv/** - it's in .gitignore (if you use git)

---

## ✅ Installation Checklist

- [ ] Installed python3-pip
- [ ] Installed python3-venv
- [ ] Created virtual environment
- [ ] Activated virtual environment
- [ ] Installed Python packages
- [ ] Installed Playwright browsers
- [ ] Verified all installations
- [ ] Ready to run tests!

---

## 🎯 Quick Test After Installation

Run this to verify everything works:

```bash
source venv/bin/activate
pytest tests/test_01_login.py::TestTariffManagementLogin::test_login_page_loads --headed
```

This will:
- Open browser
- Navigate to login page
- Take screenshot
- Close browser

If this works, everything is installed correctly! ✅

---

## 📞 Need Help?

Check these files:
- `README.md` - Project overview
- `docs/EXECUTION_GUIDE.md` - How to run tests
- `QUICK_START.txt` - Quick reference

---

**Happy Testing! 🚀**
