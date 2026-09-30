# Tariff Management - Playwright Automation Testing

## 📋 Project Overview
Comprehensive Playwright automation test suite for the HummingBird ERP Tariff Management module with bug tracking and visual validation.

## 🌐 Test Environment
- **Application URL**: https://test-warsoft-v4.hummingbirdindia.com/property/tariff
- **Credentials**: 
  - Email: `anu@hummingbirdindia.com`
  - Password: `Anu@1234`

## 📁 Project Structure
```
Tariff_Management/
├── tests/
│   ├── __init__.py
│   ├── test_01_login.py                 # Login functionality
│   ├── test_02_tariff_management.py     # Core tariff tests
│   ├── test_03_bugs.py                  # Bug validation (1-9)
│   └── test_04_more_bugs.py             # Bug validation (10-20)
├── assets/
│   ├── screenshots/                      # Test execution screenshots
│   └── bugs/                             # Bug evidence screenshots
├── docs/
│   ├── README.md                         # Detailed documentation
│   └── BUG_REPORT.md                     # Complete bug report
├── reports/                              # HTML test reports
├── conftest.py                           # Pytest fixtures
├── pytest.ini                            # Pytest configuration
├── requirements.txt                      # Dependencies
└── README.md                             # This file
```

## 🚀 Quick Start

### Prerequisites
```bash
# Install Python 3.8+
python --version

# Install pip
pip --version
```

### Installation
```bash
# Clone or navigate to project directory
cd Tariff_Management

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install chromium
```

### Running Tests

#### Run all tests (Headed mode with slow motion):
```bash
pytest --headed --slowmo=1000 -v
```

#### Run specific test file:
```bash
pytest tests/test_01_login.py --headed --slowmo=1000
```

#### Run with HTML report:
```bash
pytest --html=reports/report.html --self-contained-html
```

#### Run specific test:
```bash
pytest tests/test_02_tariff_management.py::TestTariffManagement::test_01_navigate_to_tariff_page --headed
```

## 📊 Test Cases Summary

### Total Test Cases: 22+

| Test Suite | Tests | Description |
|------------|-------|-------------|
| Login | 2 | Login page and authentication |
| Tariff Management | 5 | Core functionality |
| Bug Validation | 15+ | All identified bugs |

## 🐛 Bugs Found: 20

| Priority | Count | Status |
|----------|-------|--------|
| High | 2 | Open |
| Medium | 10 | Open |
| Low | 8 | Open |

See [BUG_REPORT.md](docs/BUG_REPORT.md) for detailed bug information.

## 📸 Screenshots

All screenshots are automatically captured during test execution:
- **Test Screenshots**: `assets/screenshots/`
- **Bug Evidence**: `assets/bugs/`

Screenshots include timestamps in filename format: `bug_01_checkbox_not_visible_20260929_153000.png`

## ⚙️ Configuration

### Slow Motion (for visibility)
Edit `conftest.py` to adjust speed:
```python
"slow_mo": 1000,  # milliseconds (1000 = 1 second)
```

### Headless Mode
Change in `conftest.py`:
```python
"headless": False,  # Set to True for headless execution
```

## 📝 Test Features

### ✅ Implemented Features:
- Single login session for all tests
- Headed mode execution (visible browser)
- Slow motion (1 second delay) for better visibility
- Automatic screenshot capture
- HTML report generation
- Bug evidence collection
- Timestamp-based file naming
- Comprehensive test coverage

### 🎯 Testing Scope:

#### Functional Testing:
1. Login functionality
2. Property selection
3. Room charges management
4. TAC exceptions handling
5. History table verification
6. Date picker validation
7. Image upload functionality
8. Filter operations
9. Table interactions
10. Form validations

#### Bug Validation:
- All 20 bugs documented and tested
- Visual evidence captured
- Reproducible test steps
- Priority classification

## 📚 Documentation

- **[README.md](docs/README.md)**: Detailed setup and usage guide
- **[BUG_REPORT.md](docs/BUG_REPORT.md)**: Complete bug report with screenshots

## 🔧 Troubleshooting

### Issue: Browser not launching
```bash
# Reinstall browsers
playwright install --force
```

### Issue: Tests failing due to timeout
```bash
# Increase timeout in pytest.ini or individual tests
page.set_default_timeout(60000)  # 60 seconds
```

### Issue: Screenshots not saving
```bash
# Ensure directories exist
mkdir -p assets/screenshots assets/bugs reports
```

## 📈 Test Execution Flow

```
1. Setup → Install dependencies
2. Login → Single login for all tests
3. Navigate → Go to Tariff Management
4. Execute → Run test cases sequentially
5. Capture → Take screenshots at each step
6. Report → Generate HTML report
7. Validate → Check bug evidence
```

## 🎬 Execution Speed

Tests are configured with **1-second delay** between actions for:
- Better visibility
- User can follow the test execution
- Easier debugging
- Visual validation

## 📊 Reports

After test execution, find reports at:
- **HTML Report**: `reports/report.html`
- **Screenshots**: `assets/screenshots/`
- **Bug Evidence**: `assets/bugs/`

## 🔐 Security Note

Credentials are hardcoded for testing purposes only. In production:
- Use environment variables
- Use secure credential management
- Never commit credentials to version control

## 🤝 Contributing

To add new tests:
1. Create new test file in `tests/` directory
2. Follow naming convention: `test_XX_feature_name.py`
3. Add appropriate fixtures from `conftest.py`
4. Document test cases
5. Capture screenshots

## 📞 Support

For questions or issues:
- Check documentation in `docs/` folder
- Review existing test cases
- Check screenshot evidence

## 🏆 Best Practices Followed

- ✅ Page Object Model can be implemented
- ✅ Reusable fixtures
- ✅ Clear test naming
- ✅ Comprehensive documentation
- ✅ Screenshot evidence
- ✅ Slow motion for visibility
- ✅ Single login session
- ✅ Proper test organization

---

**Last Updated**: September 29, 2026  
**Version**: 1.0.0  
**Framework**: Playwright + Pytest  
**Language**: Python 3.8+
