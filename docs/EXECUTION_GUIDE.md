# Test Execution Guide

## Step-by-Step Execution Instructions

### 1. Environment Setup

#### Install Python Dependencies
```bash
cd /home/selvaganesh/Selva-Backup/Git/Playwright/Tariff_Management
pip install -r requirements.txt
```

#### Install Playwright Browsers
```bash
playwright install chromium
```

### 2. Verify Installation
```bash
# Check Playwright installation
playwright --version

# Check pytest installation
pytest --version
```

### 3. Run Tests

#### Option 1: Run All Tests (Recommended)
```bash
pytest --headed --slowmo=1000 -v -s
```

**Explanation:**
- `--headed`: Shows browser window
- `--slowmo=1000`: 1-second delay between actions
- `-v`: Verbose output
- `-s`: Show print statements

#### Option 2: Run Tests with HTML Report
```bash
pytest --headed --slowmo=1000 --html=reports/report.html --self-contained-html
```

#### Option 3: Run Specific Test Suite
```bash
# Login tests only
pytest tests/test_01_login.py --headed --slowmo=1000

# Tariff management tests only
pytest tests/test_02_tariff_management.py --headed --slowmo=1000

# Bug validation tests only
pytest tests/test_03_bugs.py tests/test_04_more_bugs.py --headed --slowmo=1000
```

#### Option 4: Run Single Test
```bash
pytest tests/test_01_login.py::TestTariffManagementLogin::test_login_page_loads --headed
```

### 4. Test Execution Behavior

#### What You'll See:
1. **Browser Opens**: Chromium browser window will open
2. **Slow Actions**: Each action takes 1 second to complete
3. **Login Once**: Login happens at the start
4. **Sequential Tests**: Tests run one after another
5. **Screenshots**: Automatically captured at each step
6. **Terminal Output**: Test progress shown in terminal

#### Execution Time:
- **Full Suite**: ~15-20 minutes (with slow motion)
- **Login Tests**: ~1-2 minutes
- **Bug Tests**: ~10-15 minutes

### 5. View Results

#### During Execution:
Watch the browser as tests execute in slow motion

#### After Execution:

##### Terminal Output:
```
tests/test_01_login.py::TestTariffManagementLogin::test_login_page_loads PASSED
tests/test_01_login.py::TestTariffManagementLogin::test_login_with_valid_credentials PASSED
tests/test_02_tariff_management.py::TestTariffManagement::test_01_navigate_to_tariff_page PASSED
...
====================== 22 passed in 900.00s (0:15:00) ======================
```

##### HTML Report:
Open `reports/report.html` in browser to see:
- Test pass/fail status
- Execution time
- Error details (if any)
- Test hierarchy

##### Screenshots:
- **Test Screenshots**: `assets/screenshots/`
- **Bug Evidence**: `assets/bugs/`

### 6. Adjust Speed (Optional)

If you want faster or slower execution:

#### Edit conftest.py:
```python
"slow_mo": 500,   # 0.5 seconds
"slow_mo": 1500,  # 1.5 seconds
"slow_mo": 2000,  # 2 seconds
```

### 7. Headless Mode (Background Execution)

For CI/CD or background execution:

#### Edit conftest.py:
```python
"headless": True,  # No browser window
```

Then run:
```bash
pytest -v --html=reports/report.html
```

### 8. Troubleshooting

#### Problem: ModuleNotFoundError
```bash
# Solution: Install requirements
pip install -r requirements.txt
```

#### Problem: Playwright not found
```bash
# Solution: Install playwright
pip install playwright
playwright install
```

#### Problem: Tests timing out
```bash
# Solution: Increase timeout
# Add to test file:
page.set_default_timeout(60000)  # 60 seconds
```

#### Problem: Screenshots not saving
```bash
# Solution: Create directories
mkdir -p assets/screenshots assets/bugs reports
```

#### Problem: Browser won't close
```bash
# Solution: Kill process manually
pkill -f chromium
```

### 9. Running Specific Bug Tests

```bash
# Test specific bug
pytest tests/test_03_bugs.py::TestTariffManagementBugs::test_06_bug_table_heading_mismatch --headed --slowmo=1000

# Test bugs 1-9
pytest tests/test_03_bugs.py --headed --slowmo=1000

# Test bugs 10-20
pytest tests/test_04_more_bugs.py --headed --slowmo=1000
```

### 10. CI/CD Integration

For automated execution:

```bash
# Fast headless execution
pytest --headless -v --html=reports/report_$(date +%Y%m%d_%H%M%S).html
```

### 11. Debug Mode

To debug failing tests:

```bash
# Run with debug output
pytest --headed --slowmo=2000 -vv -s --tb=long
```

**Options:**
- `-vv`: Very verbose
- `--tb=long`: Long traceback
- `--slowmo=2000`: Extra slow

### 12. Screenshot Review

After execution, review screenshots:

```bash
# View screenshots
ls -lh assets/screenshots/
ls -lh assets/bugs/

# Open screenshot folder
xdg-open assets/screenshots/  # Linux
open assets/screenshots/      # Mac
explorer assets\screenshots\  # Windows
```

### 13. Generate Custom Report

```bash
# With custom report name
pytest --headed --slowmo=1000 --html=reports/tariff_test_$(date +%Y%m%d).html --self-contained-html
```

### 14. Parallel Execution (Advanced)

Install pytest-xdist:
```bash
pip install pytest-xdist
```

Run tests in parallel:
```bash
pytest -n 2  # Run with 2 workers
```

**Note**: Parallel execution may not work well with headed mode and screenshots.

### 15. Watch Test Execution

The tests are designed to be watched:
- Sit back and watch browser actions
- Verify each step visually
- Screenshots capture key moments
- Slow motion makes everything visible

### 16. Best Practices

1. **Always run in headed mode first** to understand test flow
2. **Review screenshots** after execution
3. **Check HTML report** for detailed results
4. **Run bug tests separately** for focused validation
5. **Use slow motion** for demo purposes
6. **Use headless mode** for CI/CD

---

## Quick Reference Commands

```bash
# Full test suite with report
pytest --headed --slowmo=1000 --html=reports/report.html

# Login only
pytest tests/test_01_login.py --headed --slowmo=1000

# All bugs
pytest tests/test_03_bugs.py tests/test_04_more_bugs.py --headed --slowmo=1000

# Fast headless
pytest --headless -v

# Debug mode
pytest --headed --slowmo=2000 -vv -s
```

---

**Happy Testing! 🚀**
