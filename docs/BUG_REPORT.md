# Tariff Management Bug Report

## Summary
This document contains detailed information about all bugs found during testing of the Tariff Management module.

---

## BUG #1: Checkbox not clearly visible ✅ FIXED
**Priority**: Medium  
**Module**: TAC Exceptions  
**Description**: In Tariff management, TAC Exceptions Checkbox not clearly visible  
**Steps to Reproduce**:
1. Login to application
2. Navigate to Tariff Management
3. Click on TAC Exceptions tab
4. Observe the checkbox visibility

**Expected**: Checkbox should be clearly visible  
**Actual**: Checkbox is not clearly visible  
**Screenshot**: Located in `assets/bugs/bug_01_checkbox_not_visible_*.png`

---

## BUG #2: Control initial space in filter ✅ FIXED
**Priority**: Low  
**Module**: All Filters  
**Description**: Initial space is allowed in all filter fields  
**Steps to Reproduce**:
1. Navigate to any table with filter
2. Click on filter input
3. Type space as first character
4. Observe it's being accepted

**Expected**: Filter should trim or prevent initial spaces  
**Actual**: Initial spaces are allowed  
**Screenshot**: Located in `assets/bugs/bug_02_filter_initial_space_*.png`

---

## BUG #3: Table header name is in caps
**Priority**: Low  
**Module**: All Tables  
**Description**: All table header names are displayed in CAPS  
**Steps to Reproduce**:
1. Navigate to Tariff Management
2. View any table
3. Observe header names

**Expected**: Headers should follow proper title case  
**Actual**: All headers are in CAPS  
**Screenshot**: Located in `assets/bugs/bug_03_table_header_caps_*.png`

---

## BUG #4: Table heading name difference
**Priority**: Medium  
**Module**: Tables  
**Description**: Table header names mismatch between old and new site  
**Steps to Reproduce**:
1. Compare old site table headers
2. Compare new site table headers
3. Note differences

**Expected**: Headers should match old site naming  
**Actual**: Headers have different names  
**Screenshot**: Located in `assets/bugs/bug_04_table_heading_mismatch_*.png`

---

## BUG #5: Tool tip data not showing
**Priority**: Medium  
**Module**: Room Type  
**Description**: Tax inclusive tooltip is not displaying on hover  
**Steps to Reproduce**:
1. Navigate to Room charges
2. Hover over tax inclusive field
3. Wait for tooltip

**Expected**: Tooltip should display information  
**Actual**: Tooltip does not appear  
**Screenshot**: Located in `assets/bugs/bug_05_tooltip_missing_*.png`

---

## BUG #6: Design issue at background
**Priority**: Low  
**Module**: Room Details Popup  
**Description**: Background design issue when Room Details popup appears  
**Steps to Reproduce**:
1. Click 'Add room charges'
2. Observe background design
3. Note the visual issue

**Expected**: Clean background with proper overlay  
**Actual**: Design issue visible in background  
**Screenshot**: Located in `assets/bugs/bug_06_design_background_*.png`

---

## BUG #7: Error message content
**Priority**: Medium  
**Module**: Room Charges  
**Description**: Unclear error message about using existing image from grid  
**Steps to Reproduce**:
1. Click 'Add room charges'
2. Click Create without uploading image
3. Read error message

**Expected**: Clear error message explaining where to find images  
**Actual**: Confusing message "Use Existing image from grid means?"  
**Screenshot**: Located in `assets/bugs/bug_07_error_message_*.png`

---

## BUG #8: Date picker icon alignment
**Priority**: Low  
**Module**: Date Fields  
**Description**: Date picker icon is aligned in center instead of right  
**Steps to Reproduce**:
1. Observe date picker fields
2. Check icon alignment

**Expected**: Icon should be right-aligned  
**Actual**: Icon is center-aligned  
**Screenshot**: Located in `assets/bugs/bug_08_date_picker_alignment_*.png`

---

## BUG #9: Room image upload size not fit to the box
**Priority**: Medium  
**Module**: Room Image Upload  
**Description**: Uploaded room image does not fit properly in the designated box  
**Steps to Reproduce**:
1. Upload a room image
2. Observe how it fits in the box
3. Note the sizing issue

**Expected**: Image should fit properly within the box boundaries  
**Actual**: Image does not fit correctly  
**Screenshot**: Located in `assets/bugs/bug_09_room_image_fit_*.png`

---

## BUG #10: Alignment issue
**Priority**: Low  
**Module**: Room Charges  
**Description**: Single, double, triple agree values not aligned in center  
**Steps to Reproduce**:
1. View room charges table
2. Check alignment of tariff columns
3. Note alignment issue

**Expected**: Values should be center-aligned  
**Actual**: Values are not properly aligned  
**Screenshot**: Located in `assets/bugs/bug_10_alignment_issue_*.png`

---

## BUG #11: Tool tip not shown in Room charge details table
**Priority**: Medium  
**Module**: Room Charge Details  
**Description**: Tooltip not showing on hover over Edit/Delete icons  
**Steps to Reproduce**:
1. Navigate to Room charge details table
2. Hover over Edit icon
3. Hover over Delete icon
4. No tooltip appears

**Expected**: Tooltip should show "Edit" and "Delete"  
**Actual**: No tooltip appears  
**Screenshot**: Located in `assets/bugs/bug_11_tooltip_room_charge_*.png`

---

## BUG #12: To Date captured wrongly in screen
**Priority**: High  
**Module**: Room Charges - Date Fields  
**Description**: Valid End Date shows different date in screen vs database  
**Steps to Reproduce**:
1. Select Valid End Date as 13/03/2026
2. Save the room charge
3. Database shows correct date (13/03/2026)
4. Screen shows 28/02/2027 (1 year from start date)
5. Room ID: 387445

**Expected**: Screen should show the selected date (13/03/2026)  
**Actual**: Screen displays 28/02/2027  
**Screenshot**: Located in `assets/bugs/bug_12_to_date_wrong_*.png`

---

## BUG #13: Tariff fields amount able to enter more
**Priority**: Medium  
**Module**: Tariff Input Fields  
**Description**: Tariff fields allow entering excessive length without validation  
**Steps to Reproduce**:
1. Click on any tariff field (Single/Double/Triple)
2. Enter very large numbers
3. No length validation applied
4. Rate Tariff validation not checked

**Expected**: Should have length limit (9 digits including comma)  
**Actual**: Allows unlimited length entry  
**Screenshot**: Located in `assets/bugs/bug_13_tariff_length_*.png`

---

## BUG #14: Remove pagination in Room charge Details
**Priority**: Low  
**Module**: Room Charge Details Table  
**Description**: Pagination is not needed in Room charge details table  
**Steps to Reproduce**:
1. Navigate to Room charge details table
2. Observe pagination at bottom
3. It's unnecessary for this table

**Expected**: No pagination for small datasets  
**Actual**: Pagination is present  
**Screenshot**: Located in `assets/bugs/bug_14_pagination_*.png`

---

## BUG #15: TAC Percentage dot not allowing issue
**Priority**: High  
**Module**: TAC Percentage Field  
**Description**: Decimal point (.) is not allowed in TAC Per field but error asks for it  
**Steps to Reproduce**:
1. Enter TAC percentage value
2. Try to enter decimal (e.g., 12.5)
3. Decimal point is not accepted
4. Click Create
5. Error message appears asking for decimal format

**Expected**: Either allow decimal or don't ask for it in error  
**Actual**: Contradictory behavior - field blocks decimal but error requests it  
**Screenshot**: Located in `assets/bugs/bug_15_tac_percentage_dot_*.png`

---

## BUG #16: Date manually allowing to edit
**Priority**: Medium  
**Module**: Date Picker Fields  
**Description**: Date fields allow manual typing which can lead to invalid dates  
**Steps to Reproduce**:
1. Click on date field
2. Try typing manually
3. Invalid date can be entered

**Expected**: Date should only be selectable from calendar picker  
**Actual**: Manual typing is allowed  
**Screenshot**: Located in `assets/bugs/bug_16_date_manual_edit_*.png`

---

## BUG #17: Filter not cleared after property name selected
**Priority**: Low  
**Module**: Property Filter  
**Description**: Filter text remains after property selection  
**Steps to Reproduce**:
1. Enter text in filter field
2. Type and select property name
3. Filter text is not cleared automatically

**Expected**: Filter should clear after selection  
**Actual**: Filter text remains  
**Screenshot**: Located in `assets/bugs/bug_17_filter_not_cleared_*.png`

---

## BUG #18: Design overlaps
**Priority**: Medium  
**Module**: Table Display  
**Description**: Column headers overlap when horizontally scrolled  
**Steps to Reproduce**:
1. Navigate to room charges table
2. Scroll horizontally from left to right
3. Observe column header overlapping

**Expected**: Headers should not overlap during scroll  
**Actual**: Headers overlap each other  
**Screenshot**: Located in `assets/bugs/bug_18_design_overlaps_*.png`

---

## BUG #19: Design Issue in Firefox
**Priority**: Medium  
**Module**: UI - Browser Compatibility  
**Description**: Design issues visible specifically in Firefox browser  
**Steps to Reproduce**:
1. Open application in Firefox browser
2. Navigate to Tariff Management
3. Observe design issues

**Expected**: Consistent design across all browsers  
**Actual**: Design issues in Firefox  
**Screenshot**: Located in `assets/bugs/bug_19_firefox_design_*.png`

---

## BUG #20: Room image upload inside the box - Text issue
**Priority**: Low  
**Module**: Room Image Upload  
**Description**: "Room" text is showing inside the image upload box  
**Steps to Reproduce**:
1. Navigate to Add Room Charges
2. Look at room image upload box
3. Observe text display

**Expected**: Clean image upload box without text overlay  
**Actual**: "Room" text appears inside the box  
**Screenshot**: Located in `assets/bugs/bug_20_room_image_text_*.png`

---

## Bug Priority Summary

| Priority | Count |
|----------|-------|
| High     | 2     |
| Medium   | 10    |
| Low      | 8     |
| **Total**| **20**|

## Test Coverage

### Modules Tested:
- Login
- Property Selection
- Room Charges Management
- TAC Exceptions
- History Table
- Date Pickers
- Image Upload
- Filters and Search
- Table Display
- Form Validations

## Recommendations

1. **High Priority Bugs** should be fixed in next sprint
2. **Medium Priority Bugs** affecting user experience should be addressed soon
3. **Low Priority Bugs** can be scheduled for future releases
4. Implement comprehensive field validation
5. Add proper tooltips across all UI elements
6. Ensure cross-browser compatibility testing
7. Implement consistent design standards

---

**Report Generated**: September 29, 2026  
**Tested By**: Automation Team  
**Test Environment**: https://test-warsoft-v4.hummingbirdindia.com
