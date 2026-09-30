# Test Case Documentation

## Login Test Cases

### TC_001: Verify Login Page Loads
**Objective**: Verify that the login page loads successfully  
**Priority**: High  
**Test Data**: URL: https://test-warsoft-v4.hummingbirdindia.com/property/tariff

**Steps**:
1. Navigate to application URL
2. Wait for page to load

**Expected Result**:
- Page title is "HummingBird - ERP - Warsoft ?v=4.0.29"
- "Welcome back!" text is visible
- Email and password fields are present

**Screenshot**: `01_login_page_*.png`

---

### TC_002: Login with Valid Credentials
**Objective**: Verify login functionality with valid credentials  
**Priority**: High  
**Test Data**: 
- Email: anu@hummingbirdindia.com
- Password: Anu@1234

**Steps**:
1. Navigate to login page
2. Enter valid email
3. Enter valid password
4. Click Sign In button
5. Wait for redirect

**Expected Result**:
- User is logged in successfully
- Redirected away from login page
- Dashboard or home page loads

**Screenshots**: 
- `02_before_login_*.png`
- `03_after_login_*.png`

---

## Tariff Management Test Cases

### TC_003: Navigate to Tariff Management Page
**Objective**: Verify navigation to tariff management module  
**Priority**: High

**Steps**:
1. Login to application
2. Navigate to /property/tariff
3. Wait for page load

**Expected Result**:
- Tariff management page loads
- Property selection dropdown visible
- Add Room Charges button visible

**Screenshot**: `04_tariff_page_*.png`

---

### TC_004: Select Property
**Objective**: Verify property selection from dropdown  
**Priority**: Medium

**Steps**:
1. Navigate to tariff page
2. Click on Property Name dropdown
3. Select a property from list

**Expected Result**:
- Dropdown opens with property list
- Property can be selected
- Room charges load for selected property

**Screenshot**: `05_property_dropdown_*.png`

---

## Bug Validation Test Cases

### TC_BUG_001: Checkbox Visibility Issue
**Bug ID**: BUG #1  
**Priority**: Medium  
**Module**: TAC Exceptions

**Steps**:
1. Navigate to tariff management
2. Click on TAC Exceptions tab
3. Observe checkbox visibility

**Expected Result**: Checkbox should be clearly visible  
**Actual Result**: Checkbox not clearly visible  
**Status**: FAIL - Bug Confirmed

**Screenshot**: `bug_01_checkbox_not_visible_*.png`

---

### TC_BUG_002: Filter Initial Space
**Bug ID**: BUG #2  
**Priority**: Low  
**Module**: Filters

**Steps**:
1. Click on any filter field
2. Type space as first character
3. Observe if it's accepted

**Expected Result**: Initial space should be trimmed/prevented  
**Actual Result**: Initial space is allowed  
**Status**: FAIL - Bug Confirmed

**Screenshot**: `bug_02_filter_initial_space_*.png`

---

### TC_BUG_003: Table Headers in Caps
**Bug ID**: BUG #3  
**Priority**: Low  
**Module**: All Tables

**Steps**:
1. Navigate to any table
2. Observe header text casing

**Expected Result**: Headers should be in Title Case  
**Actual Result**: All headers are in UPPERCASE  
**Status**: FAIL - Bug Confirmed

**Screenshot**: `bug_03_table_header_caps_*.png`

---

### TC_BUG_004: Table Heading Mismatch
**Bug ID**: BUG #4  
**Priority**: Medium  
**Module**: Tables

**Steps**:
1. Compare headers with old site
2. Note differences

**Expected Result**: Headers should match old site  
**Actual Result**: Headers have different names  
**Status**: FAIL - Bug Confirmed

**Screenshot**: `bug_04_table_heading_mismatch_*.png`

---

### TC_BUG_005: Missing Tooltip
**Bug ID**: BUG #5  
**Priority**: Medium  
**Module**: Room Charges

**Steps**:
1. Navigate to room charges
2. Hover over tax inclusive field
3. Wait for tooltip

**Expected Result**: Tooltip should appear with information  
**Actual Result**: No tooltip appears  
**Status**: FAIL - Bug Confirmed

**Screenshot**: `bug_05_tooltip_missing_*.png`

---

### TC_BUG_006: Background Design Issue
**Bug ID**: BUG #6  
**Priority**: Low  
**Module**: Popup

**Steps**:
1. Click "Add room charges"
2. Observe background

**Expected Result**: Clean background overlay  
**Actual Result**: Design issue in background  
**Status**: FAIL - Bug Confirmed

**Screenshot**: `bug_06_design_background_*.png`

---

### TC_BUG_007: Error Message Unclear
**Bug ID**: BUG #7  
**Priority**: Medium  
**Module**: Room Charges

**Steps**:
1. Click "Add room charges"
2. Click Create without image
3. Read error message

**Expected Result**: Clear error message  
**Actual Result**: Confusing message about grid image  
**Status**: FAIL - Bug Confirmed

**Screenshot**: `bug_07_error_message_*.png`

---

### TC_BUG_008: Date Picker Alignment
**Bug ID**: BUG #8  
**Priority**: Low  
**Module**: Date Fields

**Steps**:
1. Observe date picker icon position

**Expected Result**: Icon should be right-aligned  
**Actual Result**: Icon is center-aligned  
**Status**: FAIL - Bug Confirmed

**Screenshot**: `bug_08_date_picker_alignment_*.png`

---

### TC_BUG_009: Room Image Not Fitting
**Bug ID**: BUG #9  
**Priority**: Medium  
**Module**: Image Upload

**Steps**:
1. Upload room image
2. Observe how it fits

**Expected Result**: Image fits within box boundaries  
**Actual Result**: Image doesn't fit correctly  
**Status**: FAIL - Bug Confirmed

**Screenshot**: `bug_09_room_image_fit_*.png`

---

### TC_BUG_010: Tariff Alignment Issue
**Bug ID**: BUG #10  
**Priority**: Low  
**Module**: Room Charges

**Steps**:
1. View room charges table
2. Check tariff value alignment

**Expected Result**: Values center-aligned  
**Actual Result**: Values not properly aligned  
**Status**: FAIL - Bug Confirmed

**Screenshot**: `bug_10_alignment_issue_*.png`

---

### TC_BUG_011: Tooltip Missing in Table
**Bug ID**: BUG #11  
**Priority**: Medium  
**Module**: Room Charge Details

**Steps**:
1. Hover over Edit icon
2. Hover over Delete icon

**Expected Result**: Tooltips should appear  
**Actual Result**: No tooltips  
**Status**: FAIL - Bug Confirmed

**Screenshot**: `bug_11_tooltip_room_charge_*.png`

---

### TC_BUG_012: Date Display Wrong
**Bug ID**: BUG #12  
**Priority**: High  
**Module**: Date Fields

**Steps**:
1. Select end date as 13/03/2026
2. Save
3. Check display vs database

**Expected Result**: Display matches database  
**Actual Result**: Display shows different date  
**Status**: FAIL - Bug Confirmed

**Screenshot**: `bug_12_to_date_wrong_*.png`

---

### TC_BUG_013: Tariff Field Length
**Bug ID**: BUG #13  
**Priority**: Medium  
**Module**: Tariff Fields

**Steps**:
1. Enter very long number in tariff field
2. Observe validation

**Expected Result**: Length should be limited  
**Actual Result**: Unlimited length allowed  
**Status**: FAIL - Bug Confirmed

**Screenshot**: `bug_13_tariff_length_*.png`

---

### TC_BUG_014: Unnecessary Pagination
**Bug ID**: BUG #14  
**Priority**: Low  
**Module**: Room Charge Table

**Steps**:
1. View room charge details table
2. Observe pagination

**Expected Result**: No pagination needed  
**Actual Result**: Pagination present  
**Status**: FAIL - Bug Confirmed

**Screenshot**: `bug_14_pagination_*.png`

---

### TC_BUG_015: TAC Decimal Issue
**Bug ID**: BUG #15  
**Priority**: High  
**Module**: TAC Percentage

**Steps**:
1. Try entering decimal in TAC field
2. Click Create
3. Read error

**Expected Result**: Either allow decimal or don't ask for it  
**Actual Result**: Field blocks decimal but error requests it  
**Status**: FAIL - Bug Confirmed

**Screenshot**: `bug_15_tac_percentage_dot_*.png`

---

### TC_BUG_016: Manual Date Edit
**Bug ID**: BUG #16  
**Priority**: Medium  
**Module**: Date Picker

**Steps**:
1. Click on date field
2. Try typing manually

**Expected Result**: Only calendar selection allowed  
**Actual Result**: Manual typing allowed  
**Status**: FAIL - Bug Confirmed

**Screenshot**: `bug_16_date_manual_edit_*.png`

---

### TC_BUG_017: Filter Not Cleared
**Bug ID**: BUG #17  
**Priority**: Low  
**Module**: Property Filter

**Steps**:
1. Enter text in filter
2. Select property
3. Check if filter cleared

**Expected Result**: Filter cleared after selection  
**Actual Result**: Filter text remains  
**Status**: FAIL - Bug Confirmed

**Screenshot**: `bug_17_filter_not_cleared_*.png`

---

### TC_BUG_018: Header Overlap
**Bug ID**: BUG #18  
**Priority**: Medium  
**Module**: Table Scroll

**Steps**:
1. Scroll table horizontally
2. Observe headers

**Expected Result**: Headers don't overlap  
**Actual Result**: Headers overlap  
**Status**: FAIL - Bug Confirmed

**Screenshot**: `bug_18_design_overlaps_*.png`

---

### TC_BUG_019: Firefox Design Issue
**Bug ID**: BUG #19  
**Priority**: Medium  
**Module**: Browser Compatibility

**Steps**:
1. Open in Firefox
2. Observe design

**Expected Result**: Consistent design  
**Actual Result**: Design issues in Firefox  
**Status**: FAIL - Bug Confirmed

**Screenshot**: `bug_19_firefox_design_*.png`

---

### TC_BUG_020: Image Upload Text
**Bug ID**: BUG #20  
**Priority**: Low  
**Module**: Image Upload

**Steps**:
1. View image upload box
2. Observe text display

**Expected Result**: Clean upload box  
**Actual Result**: "Room" text visible  
**Status**: FAIL - Bug Confirmed

**Screenshot**: `bug_20_room_image_text_*.png`

---

## Test Summary

| Category | Total | Pass | Fail |
|----------|-------|------|------|
| Login | 2 | TBD | TBD |
| Navigation | 2 | TBD | TBD |
| Bug Validation | 20 | 0 | 20 |
| **Total** | **24** | **TBD** | **20** |

## Test Coverage

### Modules:
- ✅ Login
- ✅ Property Selection
- ✅ Room Charges
- ✅ TAC Exceptions
- ✅ History Table
- ✅ Date Pickers
- ✅ Image Upload
- ✅ Filters
- ✅ Tables
- ✅ Form Validation

### Test Types:
- ✅ Functional Testing
- ✅ UI Testing
- ✅ Validation Testing
- ✅ Bug Validation
- ✅ Visual Testing

---

**Document Version**: 1.0  
**Last Updated**: September 29, 2026  
**Status**: Active Testing
