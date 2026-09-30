# Quick Test Execution Guide

## Run All 41 Tests (One Shot)

```bash
cd /home/selvaganesh/Selva-Backup/Git/Playwright/Tariff_Management
source venv/bin/activate
pytest tests/test_11_all_bugs_complete.py -v
```

**Expected:** 39 passed, 2 failed (~24 minutes)

---

## Run Specific Test Categories

### Bug Tests 1-10 (UI & Display)
```bash
pytest tests/test_11_all_bugs_complete.py::TestAllBugs::test_bug_01_checkbox_not_visible -v -s
pytest tests/test_11_all_bugs_complete.py::TestAllBugs::test_bug_02_filter_initial_space -v -s
# ... through test_bug_10
```

### Bug Tests 11-20 (Data & Validation)
```bash
pytest tests/test_11_all_bugs_complete.py -k "test_bug_1" -v
```

### Bug Tests 21-30 (Functional)
```bash
pytest tests/test_11_all_bugs_complete.py -k "test_bug_2" -v
```

### Bug Tests 31-40 (Responsive & Accessibility)
```bash
pytest tests/test_11_all_bugs_complete.py -k "test_bug_3" -v
```

### Create Room Workflow Only
```bash
pytest tests/test_11_all_bugs_complete.py::TestAllBugs::test_create_new_room_complete_workflow -v -s
```

---

## Run Failed Tests Only

```bash
pytest tests/test_11_all_bugs_complete.py::TestAllBugs::test_bug_01_checkbox_not_visible -v -s
pytest tests/test_11_all_bugs_complete.py::TestAllBugs::test_bug_12_to_date_wrong -v -s
```

---

## Features

✅ **Single Login** - One session for all 41 tests  
✅ **No Page Refresh** - SPA state maintained  
✅ **Normal Cursor** - Standard Playwright cursor  
✅ **Screenshots** - Full-page captures in `assets/bugs/`  
✅ **HTML Report** - Generated in `reports/report.html`

---

## Test Statistics

- **Total Tests:** 41
- **Bug Tests:** 40 (covering all documented bugs)
- **Workflow Tests:** 1 (complete create room workflow)
- **Success Rate:** 95% (39/41 passed)
- **Execution Time:** ~24 minutes
- **Screenshots:** 50+ full-page captures

---

## Files

- **Test Suite:** `tests/test_11_all_bugs_complete.py`
- **Config:** `conftest.py` (session login)
- **Screenshots:** `assets/bugs/bug_*.png`
- **Report:** `reports/report.html`
- **Summary:** `TEST_EXECUTION_SUMMARY.md`

---

## Viewing Results

### HTML Report
```bash
firefox reports/report.html
# or
google-chrome reports/report.html
```

### Screenshots
```bash
# Latest screenshots
ls -lt assets/bugs/bug_* | head -20

# Create room workflow
ls assets/bugs/bug_create_step*.png

# Specific bug
ls assets/bugs/bug_23_*.png
```

---

## Quick Commands

```bash
# List all tests
pytest tests/test_11_all_bugs_complete.py --collect-only

# Run with verbose output
pytest tests/test_11_all_bugs_complete.py -v -s

# Run specific test
pytest tests/test_11_all_bugs_complete.py::TestAllBugs::test_create_new_room_complete_workflow -v -s

# Generate HTML report
pytest tests/test_11_all_bugs_complete.py --html=reports/report.html --self-contained-html

# Run headless
pytest tests/test_11_all_bugs_complete.py --browser chromium --headed=false
```

---

## Test Credentials

**URL:** `https://test-warsoft-v4.hummingbirdindia.com/property/tariff`  
**Email:** `anu@hummingbirdindia.com`  
**Password:** `Anu@1234`  
**Test Property:** `AM Property`

---

## Notes

- Tests use Chromium in headed mode with `slow_mo=1000ms`
- Browser window size: 1920x1080
- Responsive tests change viewport temporarily
- All tests use session scope fixture (one login)
- Modal cleanup helper prevents overlay issues
