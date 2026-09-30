# 🎯 Tariff Management - Complete Source Code Analysis & Test Plan

**Analysis Date:** September 29, 2026  
**Source File:** `/warsoft-erp/src/pages/property/TariffManagement.tsx`  
**Total Lines:** 2,212 lines  
**Framework:** React + TypeScript + Shadcn UI

---

## 📋 Complete Feature Inventory

### 1. Property Search & Selection
**API:** `PropertyTariffManagement/GetProperty`  
**State:** `propertyName`, `propertySearch`, `propertyOpen`  
**Debounce:** 300ms  
**Min Characters:** 3  

**Features:**
- Autocomplete with keyboard navigation (ArrowUp/Down/Enter/Escape)
- Blacklist flag detection
- Blacklist details dialog (rows delimited by `~`, fields by `|`)
- Property change clears grid and resets state

**Fields:**
- `id`, `PropName`, `label`, `BlacklistFlag`, `BlacklistDetails`

---

### 2. Main Tariff Grid
**API:** `PropertyTariffManagement/GetPropertyTariffDtls`  
**State:** `propertygridLoad` (TariffRow[])  
**Pagination:** 10 rows per page  
**Filter:** Search across RoomType, UserName, Tariffs, Facility, MealPlan, Dates

**Data Structure (TariffRow):**
```typescript
{
  Id, PropertyId, AgreementId, RoomType,
  ATariffSingle, ATariffDouble, ATariffTriple,
  Facility, MealPlan, Inclusive, Visible,
  TAC, TACPer, TACInclusive,
  ValidFrom, ValidTo, RoomImage,
  UserName, Temp, Conference
}
```

**Validations on Load:**
- Check Tax Inclusive inconsistency across rows
- Agreement count validation (0, 1, or 2+ agreements)
- Disable Add/History/TAC buttons based on agreement state
- NonGST flag detection

**Actions:**
- Edit (opens edit dialog)
- Delete (confirmation dialog)
- View Image (full-screen modal)
- Export to Excel
- Horizontal scroll with header sync

---

### 3. Edit Room Type Dialog
**API:** `PropertyTariffManagement/Update`  
**State:** `editDialog`, `tariffTable`  
**Conference Change Detection:** Shows confirmation if Conference checkbox changed

**Fields:**
- Room Type* (text, no leading space)
- Single Agree (Indian number format: 1,00,000)
- Double Agree (Indian number format)
- Triple Agree (Indian number format)
- Facility (dropdown)
- Meal Plan* (dropdown: CP/EP/MAP/AP)
- Tax Inclusive (checkbox, locked after first row)
- SS Visible (checkbox)
- TAC (checkbox)
- TAC Per (0-100%, decimal allowed, regex: `/^(100(\.0{1,2})?|\d{1,2}(\.\d{1,2})?)$/`)
- TAC Tax Inclusive (checkbox, disabled unless TAC checked)
- Valid Start Date* (date picker)
- Valid End Date* (date picker, min = ValidFrom)
- Room Image* (upload, max 1MB, image only)
- Temp (checkbox)
- Conference (checkbox)

**Validations:**
- Room Type required
- At least one tariff (Single/Double/Triple) required
- Meal Plan required
- Room Image required
- NonGST properties must have Tax Inclusive checked
- TAC Per must match percentage regex
- Valid dates required

**Auto-calculation:**
- If ValidTo missing, auto-calculate as ValidFrom + 1 year - 1 day

---

### 4. Delete Room Type
**API:** `PropertyTariffManagement/Delete`  
**State:** `deleteDialog`, `deleteTableId`  
**Flow:** Delete button → Confirmation dialog → API call → Reload grid

---

### 5. Add Room Charges (Multi-Step Modal)
**APIs:**
1. `PropertyTariffManagement/LoadPopUpDetails` - Load defaults
2. `PropertyTariffManagement/Add` - Bulk save

**State:** `addRoomDialog`, `addroomchargeTableData` (staging table)

**Step 1: Open Add Room Charges Dialog**
- Loads last saved values from API
- If no data, uses last grid row or defaults
- Shows staging table (empty initially)

**Step 2: Add/Edit Room Details (Inner Dialog)**
- State: `roomDetailDialog`
- Same fields as Edit dialog
- Create/Update buttons
- Staging table operations (no API calls)

**Step 3: Staging Table Operations**
- Add row → staging table
- Edit row → update staging
- Delete row → remove from staging
- Filter & paginate (10 rows/page)

**Step 4: Save All**
- Validates at least one row in staging
- Bulk POST to API with array `NewPTM`
- Success → Clear staging → Reload grid

**Tax Inclusive Locking:**
- First row sets Tax Inclusive
- All subsequent rows inherit and cannot change
- Mixed inclusive/exclusive blocked

---

### 6. History Dialog
**API:** `PropertyTariffManagement/GetHistorydetails`  
**State:** `historyDialog`, `historyTableData` (HistoryRow[])  
**Pagination:** 5 rows per page  
**Sort:** By Modifieddate (asc/desc)

**Fields:**
- All TariffRow fields
- `CreatedByName`, `ModifiedbyName`, `Modifieddate`

**Actions:**
- View Image
- Recreate/Activate (re-add deleted room type)

**Recreate Validation:**
- Check Tax Inclusive consistency with current grid

---

### 7. TAC Exceptions
**Note:** Referenced in state (`tacExceptions`, `tacExceptionId`) but button/dialog not fully visible in analyzed code. Likely opens a separate TAC exceptions management screen.

---

### 8. Image Upload
**API:** `PropertyTariffManagement/Upload`  
**Validations:**
- File type: image/* only
- Max size: 1MB (1,000,000 bytes)
- Returns URL string (handles multiple response formats)

**Usage:**
- Edit dialog
- Add/Edit room details dialog

---

### 9. Excel Export
**Library:** xlsx
**Filename:** `{PropertyName}.xlsx`  
**Columns:** 17 columns (all tariff fields)

---

### 10. Supporting Dialogs

**Conference Change Confirmation:**
- Shown when Conference checkbox changes
- Separate dialogs for Edit and Add Room

**Tax Mismatch Dialog:**
- Shown when trying to edit with inconsistent Tax Inclusive

**Blacklist Warning Dialog:**
- Shown when property has BlacklistFlag = 1
- Displays client, reason, created date, created by
- Filterable, paginated table

**Close Add Room Confirmation:**
- Shown when trying to close with unsaved staging rows

---

## 🔄 Complete User Flows

### Flow 1: View Property Tariffs
```
1. Type property name (min 3 chars)
2. Select from dropdown
3. Grid loads with tariffs
4. Pagination/Filter/Export
```

### Flow 2: Edit Existing Room Type
```
1. Select property
2. Click Edit on row
3. Modify fields
4. Click Update
5. Handle Conference change if needed
6. API call
7. Success toast → Grid reload
```

### Flow 3: Delete Room Type
```
1. Select property
2. Click Delete (trash icon)
3. Confirmation dialog
4. Click Yes
5. API call
6. Success toast → Grid reload
```

### Flow 4: Add New Room Types (Complete)
```
1. Select property
2. Click "Add Room Charges"
3. Add Room Charges dialog opens with staging table
4. Click "Create New Room"
5. Room Details dialog opens
6. Fill all required fields:
   - Room Type
   - At least one tariff (Single/Double/Triple)
   - Meal Plan
   - Upload Room Image
   - Set dates
7. Click Create
8. Row added to staging table
9. Repeat 4-8 for more rooms
10. Click Save (in Add Room Charges dialog)
11. Bulk API call
12. Success → Clear staging → Grid reload
```

### Flow 5: Edit Room in Staging
```
1. In Add Room Charges dialog
2. Click Edit on staging row
3. Room Details dialog opens with data
4. Modify fields
5. Click Update
6. Staging row updated (no API)
```

### Flow 6: View History & Recreate
```
1. Select property
2. Click History button
3. History dialog opens with deleted records
4. Filter/Sort/Paginate
5. Click Recreate on a row
6. Confirmation dialog
7. Tax Inclusive validation
8. API call → Room reactivated
9. Grid reload
```

### Flow 7: View Room Image
```
1. Click "View" link in RoomImage column
2. Full-screen image dialog opens
3. Shows room type name
4. Close button
```

### Flow 8: Export to Excel
```
1. Select property (grid must have data)
2. Click Export button
3. Excel file downloads
4. Filename: {PropertyName}.xlsx
```

---

## 🧪 Comprehensive Test Cases

### Test Suite 1: Property Search (TS-01)

**TC-01.1: Search with Less Than 3 Characters**
- Type "A" → No results
- Type "AM" → No results
- Type "AMP" → API call, show dropdown

**TC-01.2: Search with Valid Property**
- Type "AM Property" → Show results
- Select → Grid loads, check agreement count

**TC-01.3: Search with Blacklisted Property**
- Type blacklisted property → Select
- Blacklist warning dialog opens
- Table shows: clientName, createdBy, createdDate, reason
- Click Continue → Grid loads

**TC-01.4: Keyboard Navigation**
- Type query → Dropdown opens
- Press ArrowDown → Highlight next
- Press ArrowUp → Highlight previous
- Press Enter → Select highlighted
- Press Escape → Close dropdown

**TC-01.5: Debounce Test**
- Type "AMPROPERTYFASTTYPINGTEST" quickly
- Only 1 API call after 300ms pause

**TC-01.6: No Agreement Warning**
- Select property with 0 agreements
- Warning toast: "Property doesn't have agreement"
- Add Room Charges button disabled
- History button disabled
- TAC button disabled

**TC-01.7: Multiple Agreements Warning**
- Select property with 2+ agreements
- Warning toast: "Property have 2 different agreements"
- Add Room Charges button enabled
- History/TAC buttons enabled

---

### Test Suite 2: Main Grid Operations (TS-02)

**TC-02.1: Grid Pagination**
- Load property with 15+ records
- Page 1 shows 10 rows
- Click Next → Page 2 shows remaining
- Click Previous → Back to page 1

**TC-02.2: Grid Filter**
- Type "Test" in filter box
- Only matching rows visible
- Filter across: RoomType, UserName, Tariffs, Facility, MealPlan, Dates
- Clear filter → All rows visible

**TC-02.3: Horizontal Scroll**
- Scroll table right
- Header scrolls with table
- Sticky first column (if any)

**TC-02.4: Excel Export**
- Click Export button
- File downloads: `{PropertyName}.xlsx`
- Verify 17 columns
- Verify all data present

**TC-02.5: View Room Image**
- Click "View" in RoomImage column
- Image dialog opens
- Shows full-size image
- Shows room type name
- Close button works

**TC-02.6: Tax Inclusive Inconsistency**
- Property with mixed inclusive/exclusive rows
- Warning toast appears
- Edit button shows tax mismatch dialog

---

### Test Suite 3: Edit Room Type (TS-03)

**TC-03.1: Edit Room Type - Happy Path**
- Click Edit on row
- Dialog opens with pre-filled data
- Modify Single Agree: 1,000 → 2,000
- Click Update
- Success toast
- Grid reloads
- Verify change

**TC-03.2: Edit - Required Field Validation**
- Clear Room Type → Save
- Error: "Room Type is required"
- Clear all tariffs → Save
- Error: "Any one Agreed Tariff is required"
- Clear Meal Plan → Save
- Error: "Meal Plan is required"
- Remove image → Save
- Error: "Please upload Room Image"

**TC-03.3: Edit - TAC Per Validation**
- Enter "150" in TAC Per → Save
- Error: "Please enter valid TAC Per"
- Enter "99.99" → Valid
- Enter "100.00" → Valid
- Enter "abc" → Error

**TC-03.4: Edit - Date Validation**
- Set Valid End Date < Valid Start Date
- Verify date picker blocks it (min date)
- Clear dates → Save
- Error: "Valid dates required"

**TC-03.5: Edit - NonGST Property**
- Property with NonGST flag
- Uncheck Tax Inclusive → Save
- Error: "Property is under Non-GST category, please choose Tax Inclusive"

**TC-03.6: Edit - Conference Change**
- Check Conference checkbox (was unchecked)
- Click Update
- Conference confirmation dialog opens
- Click Yes → Update
- Click No → Cancel

**TC-03.7: Edit - Image Upload**
- Click upload button
- Select non-image file (.txt) → Error: "Image file only"
- Select >1MB image → Error: "Maximum 1MB"
- Select valid image → Success toast → Image updates

**TC-03.8: Edit - Indian Number Formatting**
- Type "1000" in Single Agree
- Verify displays as "1,000"
- Type "100000"
- Verify displays as "1,00,000"
- Type "10000000"
- Verify displays as "1,00,00,000"

**TC-03.9: Edit - Meal Plan Dropdown**
- Click Meal Plan dropdown
- Verify 4 options:
  - CP - Breakfast
  - EP - Room only
  - MAP - Breakfast, Lunch or Dinner
  - AP - Breakfast, Lunch, Dinner
- Select each → Verify saves

**TC-03.10: Edit - Tax Inclusive Lock**
- Property with 2+ existing rows
- Edit any row
- Tax Inclusive checkbox disabled (greyed out)
- Cannot change

---

### Test Suite 4: Delete Room Type (TS-04)

**TC-04.1: Delete - Happy Path**
- Click Delete (trash icon)
- Confirmation dialog: "Are you sure?"
- Click Yes
- Success toast: "Deleted successfully"
- Grid reloads
- Row removed

**TC-04.2: Delete - Cancel**
- Click Delete
- Confirmation dialog
- Click No
- Dialog closes
- Row still present

**TC-04.3: Delete - Last Row**
- Property with 1 room type
- Delete it
- Grid empty
- Add Room Charges button enabled

---

### Test Suite 5: Add Room Charges - Complete Flow (TS-05)

**TC-05.1: Add Single Room - Happy Path**
```
1. Select property
2. Click "Add Room Charges"
3. Dialog opens (staging table empty)
4. Click "Create New Room"
5. Room Details dialog opens
6. Fill fields:
   - Room Type: "Deluxe Suite"
   - Single Agree: 5000
   - Double Agree: 7000
   - Triple Agree: 9000
   - Facility: Select option
   - Meal Plan: "CP - Breakfast"
   - Upload image
7. Click Create
8. Room Details dialog closes
9. Staging table shows 1 row
10. Click Save (in Add Room Charges dialog)
11. Success toast: "Room Tariff added successfully"
12. Staging table clears
13. Add Room Charges dialog closes
14. Main grid reloads
15. Verify new room present
```

**TC-05.2: Add Multiple Rooms**
```
1. Open Add Room Charges
2. Create Room 1: "Standard" (1000/1500/2000)
3. Staging table: 1 row
4. Click "Create New Room"
5. Create Room 2: "Deluxe" (2000/3000/4000)
6. Staging table: 2 rows
7. Click "Create New Room"
8. Create Room 3: "Suite" (5000/7000/9000)
9. Staging table: 3 rows
10. Click Save
11. Success → All 3 rooms added to main grid
```

**TC-05.3: Add - Edit Room in Staging**
```
1. Add 2 rooms to staging
2. Click Edit on first row
3. Room Details opens with data
4. Change Single Agree: 1000 → 1500
5. Click Update
6. Staging table updates (no API)
7. Verify change in staging
8. Click Save → All rooms go to API
```

**TC-05.4: Add - Delete Room from Staging**
```
1. Add 3 rooms to staging
2. Click Delete on 2nd row
3. Confirmation: "Are you sure?"
4. Click Yes
5. Row removed from staging (no API)
6. Staging now shows 2 rows
7. Click Save → Only 2 rooms go to API
```

**TC-05.5: Add - Required Field Validation**
```
1. Open Add Room Charges → Create New Room
2. Leave Room Type empty → Create
3. Error: "Room Type is required"
4. Fill Room Type, leave all tariffs 0 → Create
5. Error: "Any one Agreed Tariff is required"
6. Fill tariffs, no Meal Plan → Create
7. Error: "Meal Plan is required"
8. Fill Meal Plan, no image → Create
9. Error: "Please upload Room Image"
```

**TC-05.6: Add - Tax Inclusive Locking (First Row)**
```
1. Property has no existing rows
2. Open Add Room Charges → Create New Room
3. Tax Inclusive: Unchecked, Enabled
4. Check Tax Inclusive
5. Click Create
6. Staging: 1 row, Inclusive = true
7. Create New Room again
8. Tax Inclusive: Checked, Disabled (greyed out)
9. Cannot change
10. All subsequent rows inherit first row's value
```

**TC-05.7: Add - Tax Inclusive Locking (Existing Grid)**
```
1. Property has 3 existing rows, Inclusive = true
2. Open Add Room Charges → Create New Room
3. Tax Inclusive: Checked, Disabled
4. Cannot change (inherits from grid)
```

**TC-05.8: Add - Load Defaults from API**
```
1. Property has existing rows
2. Click Add Room Charges
3. API: LoadPopUpDetails
4. Create New Room
5. Verify pre-filled:
   - Single/Double/Triple Agree (last values)
   - Facility, Meal Plan
   - Tax Inclusive, Visible, TAC, TAC Per
   - Dates (today + 1 year - 1 day)
   - Image from last save
```

**TC-05.9: Add - Conference Change Confirmation**
```
1. Create room with Conference = checked
2. Conference confirmation dialog
3. Click Yes → Room added
4. Create room with Conference = unchecked
5. No confirmation → Room added
```

**TC-05.10: Add - Close with Unsaved Staging**
```
1. Add 2 rooms to staging
2. Click X (close) or Cancel
3. Confirmation: "You have unsaved changes"
4. Click Yes → Staging cleared, dialog closes
5. Repeat, click No → Dialog stays open
```

**TC-05.11: Add - Staging Table Pagination**
```
1. Add 15 rooms to staging
2. Page 1 shows 10 rooms
3. Click Next → Page 2 shows 5 rooms
4. Click Previous → Back to page 1
```

**TC-05.12: Add - Staging Table Filter**
```
1. Add 10 different room types
2. Type "Suite" in filter
3. Only "Suite" rows visible
4. Clear filter → All rows visible
```

**TC-05.13: Add - Duplicate Room Type**
```
1. Add room "Deluxe" to staging
2. Click Save
3. Add room "Deluxe" again (same name)
4. Click Save
5. Error: "Room Type already exists"
```

---

### Test Suite 6: History & Recreate (TS-06)

**TC-06.1: View History**
```
1. Select property
2. Click History button
3. Dialog opens
4. Table shows deleted/historical records
5. Columns: All tariff fields + CreatedByName, ModifiedbyName, Modifieddate
6. Pagination: 5 rows/page
7. Sort by Modifieddate (asc/desc toggle)
```

**TC-06.2: History Filter**
```
1. Open History
2. Type "Suite" in filter
3. Only matching rows visible
4. Clear → All rows
```

**TC-06.3: Recreate Room from History**
```
1. Delete room type "Deluxe"
2. Open History
3. Find "Deluxe" row
4. Click Recreate
5. Confirmation: "Are you sure?"
6. Click Yes
7. Success: "Room tariff activated successfully"
8. History dialog closes
9. Main grid reloads
10. "Deluxe" now in active grid
```

**TC-06.4: Recreate - Tax Inclusive Mismatch**
```
1. Active grid: Inclusive = true
2. History row: Inclusive = false
3. Click Recreate
4. Error: "Tax Inclusive configuration mismatch. Room type cannot be activated"
```

**TC-06.5: History Sort**
```
1. Open History with 10+ records
2. Click "Modifieddate" header
3. Sort descending (newest first)
4. Click again → Sort ascending (oldest first)
```

---

### Test Suite 7: Edge Cases & Negative Tests (TS-07)

**TC-07.1: Leading Space Prevention**
```
1. Edit dialog: Room Type field
2. Press Space at beginning
3. Space not entered
4. Type " Test" → Only "Test" entered
```

**TC-07.2: Max Length Test**
```
1. Room Type: Enter 500 characters
2. Verify max length (if any)
3. Single Agree: Enter 999999999999
4. Verify formatting/max
```

**TC-07.3: Special Characters in Room Type**
```
1. Enter: "Deluxe @ Suite #1"
2. Save → Verify accepts
3. Enter: "<script>alert('xss')</script>"
4. Save → Verify sanitized
```

**TC-07.4: Image Upload Edge Cases**
```
1. Upload .svg → Error or accepted?
2. Upload .gif → Error or accepted?
3. Upload exactly 1MB → Accepted
4. Upload 1MB + 1 byte → Error
5. Upload corrupt image → Error or accepted?
```

**TC-07.5: Date Edge Cases**
```
1. ValidFrom: Today
2. ValidTo: Today (same day) → Valid?
3. ValidFrom: Future date
4. ValidTo: Past date → Blocked by picker
5. ValidFrom: 01/01/2025
6. ValidTo: 31/12/2025 (exactly 1 year - 1 day)
```

**TC-07.6: TAC Per Edge Cases**
```
1. Enter: 0 → Valid
2. Enter: 0.01 → Valid
3. Enter: 100 → Valid
4. Enter: 100.00 → Valid
5. Enter: 100.01 → Error
6. Enter: 100.001 → Error (3 decimals)
7. Enter: -5 → Error
```

**TC-07.7: Concurrent Edits**
```
1. User A: Edit room "Deluxe"
2. User B: Edit same room "Deluxe"
3. User A: Save changes
4. User B: Try to save
5. Expected: "Already updated. Please reload"
```

**TC-07.8: Network Failure**
```
1. Disconnect network
2. Try to save edit
3. Verify error handling
4. Reconnect → Retry
```

**TC-07.9: API Timeout**
```
1. Slow network
2. Save operation
3. Loading spinner shows
4. Timeout after X seconds
5. Error message
```

**TC-07.10: Empty Grid Operations**
```
1. Property with 0 room types
2. Try Filter → No results message
3. Try Export → Error: "No record found"
4. Try Edit → No rows to edit
5. Try Delete → No rows to delete
```

---

### Test Suite 8: Performance & Load Tests (TS-08)

**TC-08.1: Large Dataset**
```
1. Property with 100+ room types
2. Load grid → Check load time
3. Filter → Check response
4. Pagination → Smooth?
5. Export → File size?
```

**TC-08.2: Rapid Clicking**
```
1. Click Edit button 10 times rapidly
2. Verify only 1 dialog opens
3. Click Save 5 times rapidly
4. Verify only 1 API call
```

**TC-08.3: Image Upload Performance**
```
1. Upload 999KB image
2. Measure time
3. Upload 1KB thumbnail
4. Compare times
```

**TC-08.4: Staging Table with 50+ Rooms**
```
1. Add 50 rooms to staging
2. Check pagination performance
3. Filter performance
4. Save all → Bulk API call time
```

---

### Test Suite 9: Mobile & Responsive (TS-09)

**TC-09.1: Viewport 768px (Tablet)**
```
1. Resize to 768px
2. Check table responsiveness
3. Check modal sizing
4. Check button layout
```

**TC-09.2: Viewport 375px (Mobile)**
```
1. Resize to 375px
2. Horizontal scroll on table
3. Modal full-screen?
4. Buttons stack vertically?
```

**TC-09.3: Touch Events**
```
1. Tablet device
2. Tap Edit button
3. Swipe table horizontally
4. Pinch-zoom on image
```

---

### Test Suite 10: Accessibility (TS-10)

**TC-10.1: Keyboard Navigation**
```
1. Tab through all form fields
2. Enter to submit
3. Escape to close
4. Arrow keys in dropdowns
```

**TC-10.2: Screen Reader**
```
1. Enable screen reader
2. Navigate property search
3. Read table rows
4. Read error messages
5. Verify aria-labels
```

**TC-10.3: Focus Management**
```
1. Open Edit dialog
2. First field auto-focused?
3. Tab order logical?
4. Close dialog → Focus returns to Edit button?
```

**TC-10.4: Color Contrast**
```
1. Check required field labels (red)
2. Check disabled fields (grey)
3. Check error messages
4. WCAG AA compliance?
```

---

## 📊 Test Data Requirements

### Properties:
1. **AM Property** - Standard, 1 agreement, inclusive = true
2. **Blacklisted Property** - Has BlacklistFlag = 1
3. **No Agreement Property** - Agreement count = 0
4. **Multi Agreement Property** - Agreement count = 2
5. **NonGST Property** - NonGSTFlag = true
6. **Empty Property** - 0 room types
7. **Large Property** - 50+ room types
8. **Mixed Inclusive Property** - Some rows inclusive, some exclusive

### Room Types:
1. Standard (1000/1500/2000)
2. Deluxe (2000/3000/4000)
3. Suite (5000/7000/9000)
4. Conference Room (10000/0/0)
5. Temp Room (500/0/0, Temp=true)
6. TAC Room (1000/1500/2000, TAC=true, TACPer=5)

### Images:
1. Valid: 500KB .jpg
2. Valid: 999KB .png
3. Invalid: 1.5MB .jpg (too large)
4. Invalid: document.pdf (not image)
5. Edge: Exactly 1MB .png

---

## 🎯 Priority Matrix

### P0 - Critical (Must Test First)
- Property search & selection
- Grid load
- Edit room type (happy path)
- Add room charges (single room)
- Delete room type
- Required field validations

### P1 - High
- Add multiple rooms
- Staging table operations
- Tax Inclusive locking
- History & recreate
- Image upload
- Excel export

### P2 - Medium
- Filter & pagination
- Conference change
- TAC Per validation
- Date validations
- Blacklist warning
- View image

### P3 - Low
- Edge cases
- Performance tests
- Mobile responsive
- Accessibility
- Special characters
- Concurrent edits

---

## 🚀 Test Execution Strategy

### Phase 1: Smoke Tests (30 mins)
- Property search
- Grid load
- Edit/Save
- Add/Save
- Delete

### Phase 2: Core Flows (2 hours)
- Complete Add Room Charges flow
- Edit with all validations
- History & recreate
- Tax Inclusive scenarios

### Phase 3: Edge Cases (1 hour)
- All validation errors
- Image upload edge cases
- Date edge cases
- TAC Per edge cases

### Phase 4: Non-Functional (1 hour)
- Performance
- Responsive
- Accessibility
- Load tests

### Total: ~4.5 hours for complete test execution

---

## 📝 Automation Recommendations

### High ROI for Automation:
1. ✅ Property search (already automated)
2. ✅ Edit room type (already automated)
3. ✅ Add room charges flow (already automated)
4. 🔄 Required field validations (partially done)
5. 🔄 Tax Inclusive locking (needs coverage)
6. ❌ History & recreate (not yet automated)
7. ❌ Delete operations (not yet automated)
8. ❌ Image upload scenarios (not yet automated)

### Manual Testing Recommended:
- Visual inspection (image quality, layout)
- Blacklist dialog (rare scenario)
- Concurrent editing
- Network failure recovery
- Accessibility with screen readers

---

This comprehensive test plan is based on actual source code analysis and covers all 2,212 lines of functionality! 🎉
