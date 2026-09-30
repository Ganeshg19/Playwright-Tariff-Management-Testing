# Tariff Management Test Automation

## Project Overview
This project contains Playwright automation tests for the HummingBird ERP Tariff Management module. Tests are written in Python and cover functional testing and bug validation.

## Test Environment
- **URL**: https://test-warsoft-v4.hummingbirdindia.com/property/tariff
- **Credentials**: 
  - Email: anu@hummingbirdindia.com
  - Password: Anu@1234

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. Install required packages:
```bash
pip install -r requirements.txt
```

2. Install Playwright browsers:
```bash
playwright install
```

## Running Tests

### Run all tests in headed mode (visible browser):
```bash
pytest --headed --slowmo=1000
```

### Run specific test file:
```bash
pytest tests/test_01_login.py --headed --slowmo=1000
```

### Run with HTML report:
```bash
pytest --html=reports/report.html --self-contained-html
```

## Test Structure

```
Tariff_Management/
├── tests/
│   ├── test_01_login.py          # Login functionality tests
│   ├── test_02_tariff_management.py  # Main tariff tests
│   └── test_03_bugs.py           # Bug validation tests
├── assets/
│   ├── screenshots/              # Test execution screenshots
│   └── bugs/                     # Bug evidence screenshots
├── reports/                      # HTML test reports
├── conftest.py                   # Pytest configuration
├── pytest.ini                    # Pytest settings
└── requirements.txt              # Python dependencies
```

## Test Cases

### Login Tests (test_01_login.py)
1. **test_login_page_loads**: Verify login page loads successfully
2. **test_login_with_valid_credentials**: Login with valid credentials

### Tariff Management Tests (test_02_tariff_management.py)
3. **test_01_navigate_to_tariff_page**: Navigate to Tariff Management page
4. **test_02_select_property**: Select property from dropdown
5. **test_03_bug_checkbox_not_visible**: BUG #1 - TAC Exceptions Checkbox visibility
6. **test_04_bug_filter_initial_space**: BUG #2 - Filter initial space control
7. **test_05_table_header_case**: BUG #3 - Table headers in caps

### Bug Validation Tests (test_03_bugs.py)
8. **test_06_bug_table_heading_mismatch**: BUG #4 - Table heading mismatch
9. **test_07_bug_tooltip_not_shown**: BUG #5 - Tooltip not showing
10. **test_08_bug_design_issue_background**: BUG #6 - Design issue at background
11. **test_09_bug_error_message_content**: BUG #7 - Error message content
12. **test_10_bug_date_picker_alignment**: BUG #8 - Date picker alignment
13. **test_11_bug_room_image_not_fit**: BUG #9 - Room image not fitting

## Bugs Identified

### BUG #1: Checkbox not clearly visible
**Status**: Open  
**Description**: In Tariff management, TAC Exceptions Checkbox not clearly visible
**Screenshot**: `assets/bugs/bug_01_checkbox_not_visible_*.png`

### BUG #2: Control initial space in filter
**Status**: Open  
**Description**: Control initial space in all filters
**Screenshot**: `assets/bugs/bug_02_filter_initial_space_*.png`

### BUG #3: Table header name is in caps
**Status**: Open  
**Description**: All table header names are in caps for this screen
**Screenshot**: `assets/bugs/bug_03_table_header_caps_*.png`

### BUG #4: Table heading name difference
**Status**: Open  
**Description**: In new site, the marked Table header name is mismatch from old site
**Screenshot**: `assets/bugs/bug_04_table_heading_mismatch_*.png`

### BUG #5: Tool tip data not showing
**Status**: Open  
**Description**: Existing room type is tax inclusive 'tool tip' is not showing
**Screenshot**: `assets/bugs/bug_05_tooltip_missing_*.png`

### BUG #6: Design issue at background
**Status**: Open  
**Description**: Design issue at background when clicking 'Add room charges'
**Screenshot**: `assets/bugs/bug_06_design_background_*.png`

### BUG #7: Error message content
**Status**: Open  
**Description**: Error message: "Use Existing image from grid means? Where is the image available"
**Screenshot**: `assets/bugs/bug_07_error_message_*.png`

### BUG #8: Date picker icon alignment
**Status**: Open  
**Description**: Date picker icon alignment is in center
**Screenshot**: `assets/bugs/bug_08_date_picker_alignment_*.png`

### BUG #9: Room image upload size not fit to the box
**Status**: Open  
**Description**: Uploaded Room image not correctly fit to the mentioned Room image box
**Screenshot**: `assets/bugs/bug_09_room_image_fit_*.png`

## Features Tested

### Tariff Management Module Features
1. Property selection
2. Add Room Charges functionality
3. TAC Exceptions management
4. History table display
5. Room type management (Edit/Delete)
6. Meal plan configuration (CP, EP, MAP, AP)
7. Valid start/end date selection
8. Tax inclusive/exclusive options
9. Room image upload
10. Excel download functionality

## Configuration

The tests are configured to run in headed mode with slow motion (1 second delay) to allow visual verification of each step. This can be adjusted in `conftest.py`:

```python
"slow_mo": 1000,  # milliseconds (1 second)
"headless": False,  # True for headless mode
```

## Reports

Test reports are generated in the `reports/` directory with timestamp. Screenshots are captured at each step and stored in `assets/screenshots/` and `assets/bugs/` directories.

## Notes

- All tests login once at the beginning using the fixture
- Screenshots are captured with timestamps
- Tests run in sequence with visible browser actions
- Slow motion is enabled for better visibility (1 second delay)
- Bug screenshots are automatically captured during test execution
