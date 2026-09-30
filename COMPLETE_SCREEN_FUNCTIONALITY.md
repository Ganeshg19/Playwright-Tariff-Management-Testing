# 📋 Tariff Management Screen - Complete Functionality Map

## All Features on the Screen

### Main Actions
1. **Add Room Charges** - Add new room pricing
2. **Edit Room Details** - Modify existing room information
3. **Add Room Property** - Add new property details
4. **Delete Room** - Remove room from list
5. **View History** - Check historical changes
6. **TAC Exceptions** - Manage TAC exceptions
7. **Search/Filter** - Filter displayed data
8. **Export** - Export data (if available)

### Screen Sections
1. **Property Selection Dropdown**
2. **Main Data Table**
   - Room Type
   - Valid From / Valid To dates
   - Single/Double/Triple occupancy rates
   - Actions (Edit, Delete, History)
3. **TAC Exceptions Tab**
4. **Filter/Search Bar**
5. **Action Buttons**

---

## Testing Plan for ALL Functionality

### Test Group 1: Property Selection & Data Loading
- Select different properties
- Verify data loads correctly
- Check empty states
- Test property switching

### Test Group 2: Add Room Charges
- Open modal
- Fill all required fields
- Test field validations
- Submit form
- Verify data appears in table

### Test Group 3: Edit Room Details
- Select existing room
- Open edit modal
- Modify fields
- Save changes
- Verify updates

### Test Group 4: Add Room Property
- Open add property modal
- Fill property details
- Test validations
- Submit
- Verify addition

### Test Group 5: Delete Functionality
- Select room to delete
- Confirm deletion
- Verify removal
- Test undo (if available)

### Test Group 6: History Viewing
- Click history button
- View historical data
- Test filtering history
- Close history view

### Test Group 7: TAC Exceptions
- Switch to TAC tab
- Add exception
- Edit exception
- Delete exception
- Test validations

### Test Group 8: Search & Filter
- Filter by room type
- Filter by date range
- Filter by occupancy
- Clear filters
- Test multiple filters

### Test Group 9: Table Operations
- Sort columns
- Horizontal scroll
- Pagination
- Row selection
- Bulk actions (if any)

### Test Group 10: Export & Other Actions
- Export to Excel/CSV
- Print functionality
- Refresh data
- Settings (if any)

---

## Proper Test Flow for Each Feature

### Example: Add Room Charges

```
Step 1: Select Property
   ↓
Step 2: Click "Add Room Charges"
   ↓
Step 3: Fill all fields:
   - Room Type dropdown
   - Valid From date
   - Valid To date
   - Single occupancy rate
   - Double occupancy rate
   - Triple occupancy rate
   - Extra bed charges (if any)
   - Tax percentage
   - etc.
   ↓
Step 4: Click Save
   ↓
Step 5: Verify success message
   ↓
Step 6: Verify new row in table
```

### Example: Edit Room Details

```
Step 1: Select Property
   ↓
Step 2: Wait for data load
   ↓
Step 3: Find room in table
   ↓
Step 4: Click Edit button
   ↓
Step 5: Verify pre-filled data
   ↓
Step 6: Modify fields
   ↓
Step 7: Click Update
   ↓
Step 8: Verify changes
```

---

## What We Need to Test

### For EACH functionality:
1. ✅ Does button exist and is visible?
2. ✅ Does button work when clicked?
3. ✅ Does modal/form open correctly?
4. ✅ Are all fields visible?
5. ✅ Do validations work?
6. ✅ Can form be submitted?
7. ✅ Does success message appear?
8. ✅ Does data persist correctly?
9. ✅ Can form be cancelled?
10. ✅ Are there any errors?

---

## Common Bugs to Look For

### Modal/Form Issues
- Modal doesn't open
- Form fields missing
- Validation not working
- Can submit empty form
- Error messages unclear
- Modal can't be closed
- Background not dimmed

### Data Issues
- Data not loading
- Wrong data displayed
- Data not saving
- Data not updating
- Duplicate entries
- Missing data

### UI Issues
- Buttons not visible
- Overlapping elements
- Responsive issues
- Alignment problems
- Color/contrast issues

### Functional Issues
- Actions not working
- Incorrect calculations
- Date issues
- Filter not working
- Sort not working
- Export failing

---

## Screenshot Strategy

### For Each Feature:
1. **Before** - Initial state
2. **During** - Action in progress
3. **After** - Result/outcome
4. **Error** - Any errors encountered

### Example: Add Room Charges
- `01_initial_state.png`
- `02_property_selected.png`
- `03_add_button_clicked.png`
- `04_modal_opened.png`
- `05_form_filled.png`
- `06_save_clicked.png`
- `07_success_message.png`
- `08_new_row_in_table.png`

---

## Priority Order

### High Priority (Must Test)
1. Add Room Charges
2. Edit Room Details
3. Delete Room
4. Property Selection
5. Table Display

### Medium Priority (Important)
1. TAC Exceptions
2. Search/Filter
3. History View
4. Form Validations

### Low Priority (Nice to Have)
1. Export functionality
2. Print preview
3. Settings
4. Bulk actions

---

## Next Steps

1. Run comprehensive test suite
2. Test EACH button on screen
3. Capture screenshots for ALL workflows
4. Document ALL bugs found
5. Annotate screenshots properly

---

**Status**: Ready to test ALL screen functionality
**Coverage**: Every button, modal, and feature
**Approach**: Proper user flow with data
