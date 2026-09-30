# Tariff Management Testing Plan - Step-by-Step Implementation

## Overview
Complete testing of Tariff Management screen with:
1. ✅ **All modal fields validation**
2. ✅ **Create new room type workflow**
3. ✅ **Update existing room type workflow**
4. ✅ **Room Charge Details modal**
5. ✅ **Annotated bug screenshots with cursor highlighting**

---

## Step 1: Understand All Modal Fields (Based on Source Code)

### Add Room Charges Modal Fields:
- **Property Name*** (auto-filled, read-only)
- **Room Type*** (text input) - Required
- **Single Agree*** (number) - Required, Indian number format
- **Double Agree*** (number) - Required, Indian number format
- **Triple Agree*** (number) - Required, Indian number format
- **Valid Start Date** (date picker) - Default: today
- **Valid End Date** (date picker) - Default: today + 1 year - 1 day
- **Facility** (dropdown) - TV Wifi parking, etc.
- **Meal Plan** (dropdown) - CP/EP/MAP/AP
- **Tax Inclusive** (checkbox)
- **TAC** (checkbox)
- **TAC Per** (number) - Only if TAC checked, max 100%
- **TAC Tax Incl** (checkbox) - Only if TAC checked
- **SB Visible** (checkbox)
- **Temp** (checkbox)
- **Conference** (checkbox)
- **Room Image** (file upload) - jpg/png, max 1MB

### Room Charge Details Modal (View/History):
- Shows table of all room charges for selected property
- Columns: Room Type, Single Agree, Double Agree, Triple Agree, Facility, Meal Plan, etc.
- Save/Cancel buttons

---

## Step 2: Create Annotated Bug Screenshot Helper

**New File:** `utils/annotated_screenshot.py`
- Draw bounding boxes around buggy elements
- Add cursor/pointer highlighting
- Add text annotations
- Save to `assets/bugs_annotated/`

---

## Step 3: Test Scenarios to Implement

### Test Suite: `test_08_complete_tariff_workflows.py`

#### Test 1: Verify All Modal Fields Exist
- Open Add Room Charges modal
- Verify all 18+ fields are present
- Screenshot with annotations

#### Test 2: Create New Room Type - Happy Path
- Select property "AM Property"
- Click "Add Room Charges"
- Fill all required fields:
  - Room Type: "Automation Test Room"
  - Single Agree: 1500
  - Double Agree: 2000
  - Triple Agree: 2500
- Select dates
- Click Save
- Verify success toast
- Screenshot each step with cursor

#### Test 3: Create New Room Type - Validation Errors
- Try to save with empty Room Type → Screenshot error
- Try to save with empty Single Agree → Screenshot error
- Try to save with empty Double Agree → Screenshot error
- Try to save with empty Triple Agree → Screenshot error
- Try to save with invalid date range → Screenshot error

#### Test 4: Update Existing Room Type
- Select property "AM Property"
- Wait for table to load
- Click Edit on first row
- Verify modal pre-filled with data
- Update Single Agree: +500
- Click Save/Update
- Verify success
- Screenshot each step

#### Test 5: Room Charge Details Modal
- Click "Room Charge Details" button
- Verify modal shows table
- Verify all columns present
- Close modal
- Screenshot

#### Test 6: TAC Field Dependencies
- Open Add modal
- Check TAC checkbox → Verify TAC Per field appears
- Uncheck TAC → Verify TAC Per field hidden
- Check TAC + enter invalid % → Screenshot error

#### Test 7: Date Picker Validation
- Open Add modal
- Set Valid End Date < Valid Start Date → Should show error
- Screenshot

#### Test 8: File Upload
- Open Add modal
- Try to upload non-image file → Should reject
- Try to upload >1MB file → Should reject
- Upload valid image → Should accept
- Screenshot

#### Test 9: Indian Number Formatting
- Type "1000" in Single Agree → Should format as "1,000"
- Type "100000" → Should format as "1,00,000"
- Screenshot

#### Test 10: Meal Plan Dropdown
- Open Add modal
- Click Meal Plan dropdown
- Verify 4 options: CP/EP/MAP/AP
- Select each and screenshot

---

## Step 4: Implementation Structure

```
tests/
├── test_08_complete_tariff_workflows.py
│   ├── TestTariffModalFields (verify all fields)
│   ├── TestCreateRoomType (create workflow)
│   ├── TestUpdateRoomType (update workflow)
│   ├── TestRoomChargeDetails (view details)
│   └── TestFieldValidations (all validations)
│
utils/
├── annotated_screenshot.py
│   ├── AnnotatedScreenshotHelper
│   ├── draw_bounding_box()
│   ├── draw_cursor()
│   ├── add_text_annotation()
│   └── highlight_element()
│
assets/
├── bugs_annotated/
│   ├── bug_01_empty_room_type_error.png
│   ├── bug_02_invalid_date_range.png
│   ├── bug_03_tac_percentage_validation.png
│   └── ... (all annotated bugs)
└── test_results/
    └── ... (existing screenshots)
```

---

## Step 5: Execution Order

1. ✅ **Step 1**: Create `utils/annotated_screenshot.py` with cursor highlighting
2. ✅ **Step 2**: Create `tests/test_08_complete_tariff_workflows.py` with all 10 tests
3. ✅ **Step 3**: Update modal closing helper in base class
4. ✅ **Step 4**: Run tests and capture annotated screenshots
5. ✅ **Step 5**: Generate bug report with all annotated images
6. ✅ **Step 6**: Update documentation

---

## Expected Outcomes

### Screenshots with Annotations:
- 🎯 Cursor visible at interaction points
- 🎯 Bounding boxes around errors/bugs
- 🎯 Text labels explaining issues
- 🎯 Arrows pointing to problematic elements

### Test Report:
- Total tests: 10
- Pass/Fail status
- Screenshots for each step
- Bug severity ratings

### Bug Report:
- List of all bugs found
- Annotated screenshots
- Steps to reproduce
- Expected vs Actual behavior

---

## Ready to Execute?

All steps are documented. Shall I proceed with implementation?
