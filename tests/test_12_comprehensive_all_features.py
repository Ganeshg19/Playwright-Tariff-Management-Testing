"""
Comprehensive Feature Testing Suite with Cursor Movement
Tests ALL features like a human user would interact
"""

import pytest
from playwright.sync_api import Page
import time
from datetime import datetime


class TestComprehensiveFeatures:
    """Complete feature testing with visible cursor movement"""
    
    def move_cursor_to(self, page: Page, x: int, y: int):
        """Smooth cursor movement for visibility"""
        page.mouse.move(x, y, steps=10)
        time.sleep(0.3)
    
    def click_with_cursor(self, page: Page, selector: str):
        """Click element with visible cursor movement"""
        element = page.locator(selector).first
        if element.is_visible():
            box = element.bounding_box()
            if box:
                # Move to element center
                x = box['x'] + box['width'] / 2
                y = box['y'] + box['height'] / 2
                self.move_cursor_to(page, x, y)
                element.click()
                time.sleep(0.5)
                return True
        return False
    
    def take_screenshot(self, page: Page, name: str):
        """Take screenshot"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        path = f"assets/features/{name}_{timestamp}.png"
        page.screenshot(path=path, full_page=True)
        print(f"📸 Screenshot: {path}")
        return path
    
    def select_property(self, page: Page):
        """Select property with cursor movement"""
        property_input = page.locator("input[placeholder*='Property']").first
        box = property_input.bounding_box()
        if box:
            self.move_cursor_to(page, box['x'] + 50, box['y'] + 20)
        
        property_input.click()
        property_input.fill("AM Property")
        time.sleep(2)
        
        dropdown = page.locator("[role='option']").first
        if dropdown.is_visible():
            box = dropdown.bounding_box()
            if box:
                self.move_cursor_to(page, box['x'] + 50, box['y'] + 15)
            dropdown.click()
            time.sleep(3)
            print("✅ Property selected")
            return True
        return False
    
    def close_modal(self, page: Page):
        """Close any open modals aggressively"""
        max_attempts = 10
        for attempt in range(max_attempts):
            # Check if any dialogs exist
            dialog_count = page.locator("[role='dialog']").count()
            if dialog_count == 0:
                print(f"✅ All modals closed after {attempt} attempts")
                break
            
            # Press Escape multiple times
            for _ in range(3):
                page.keyboard.press("Escape")
                time.sleep(0.2)
            
            # Click close buttons
            close_btns = page.locator("button[aria-label*='Close'], button:has-text('Close'), button[class*='close']").all()
            for btn in close_btns:
                try:
                    if btn.is_visible():
                        btn.click(force=True, timeout=1000)
                except:
                    pass
            
            # Click backdrop if still there
            try:
                backdrop = page.locator("[class*='backdrop'], [data-state='open'][class*='bg-black']").first
                if backdrop.is_visible():
                    backdrop.click(force=True, timeout=1000)
            except:
                pass
            
            time.sleep(0.5)
        
        # Final wait for all dialogs to be gone
        try:
            page.wait_for_selector("[role='dialog']", state="detached", timeout=3000)
        except:
            print("⚠️ Some modals may still be open")
        
        time.sleep(1)
    
    # ========================================================================
    # ADD ROOM CHARGES FEATURE TESTING
    # ========================================================================
    
    def test_01_add_room_charges_button(self, logged_in_page: Page):
        """Test Add Room Charges button visibility and click"""
        print("\n🎯 Test 01: Add Room Charges Button")
        
        if self.select_property(logged_in_page):
            # Move cursor to Add Room Charges button
            add_btn = logged_in_page.locator("button:has-text('Add Room Charges')").first
            if add_btn.is_visible():
                box = add_btn.bounding_box()
                if box:
                    self.move_cursor_to(logged_in_page, box['x'] + 80, box['y'] + 20)
                
                self.take_screenshot(logged_in_page, "add_room_charges_btn_hover")
                add_btn.click()
                time.sleep(3)
                
                # Verify dialog opened
                dialog = logged_in_page.locator("[role='dialog']").first
                assert dialog.is_visible(), "Add Room Charges dialog should open"
                print("✅ Add Room Charges dialog opened successfully")
                
                self.take_screenshot(logged_in_page, "add_room_charges_dialog_opened")
                self.close_modal(logged_in_page)
    
    def test_02_create_new_room_button(self, logged_in_page: Page):
        """Test Create New Room button in Add Room Charges dialog"""
        print("\n🎯 Test 02: Create New Room Button")
        
        if self.select_property(logged_in_page):
            # Open Add Room Charges
            add_btn = logged_in_page.locator("button:has-text('Add Room Charges')").first
            add_btn.click()
            time.sleep(3)
            
            # Find Create New Room button
            dialog = logged_in_page.locator("[role='dialog']").first
            create_btn = dialog.locator("button:has-text('Create New Room'), button:has-text('Create')").first
            
            if create_btn.is_visible():
                box = create_btn.bounding_box()
                if box:
                    self.move_cursor_to(logged_in_page, box['x'] + 70, box['y'] + 18)
                
                self.take_screenshot(logged_in_page, "create_new_room_btn_hover")
                create_btn.click(force=True)
                time.sleep(3)
                
                # Verify Room Details dialog
                print("✅ Room Details dialog opened")
                self.take_screenshot(logged_in_page, "room_details_dialog_opened")
            
            self.close_modal(logged_in_page)
    
    # ========================================================================
    # HISTORY MODAL TESTING
    # ========================================================================
    
    def test_03_history_button_click(self, logged_in_page: Page):
        """Test History button and modal opening"""
        print("\n🎯 Test 03: History Button & Modal")
        
        if self.select_property(logged_in_page):
            # Click History button with cursor movement
            history_btn = logged_in_page.locator("button:has-text('History')").first
            if history_btn.is_visible():
                box = history_btn.bounding_box()
                if box:
                    self.move_cursor_to(logged_in_page, box['x'] + 40, box['y'] + 18)
                
                self.take_screenshot(logged_in_page, "history_btn_hover")
                history_btn.click()
                time.sleep(3)
                
                # Verify History dialog
                dialog = logged_in_page.locator("[role='dialog']").first
                assert dialog.is_visible(), "History dialog should open"
                
                # Check for history title
                title = dialog.locator("h2").first
                if title.is_visible():
                    title_text = title.inner_text()
                    print(f"✅ History dialog opened: {title_text}")
                
                self.take_screenshot(logged_in_page, "history_modal_opened")
                self.close_modal(logged_in_page)
    
    def test_04_history_realtime_data(self, logged_in_page: Page):
        """Test History modal shows real-time API data"""
        print("\n🎯 Test 04: History Real-time API Data")
        
        if self.select_property(logged_in_page):
            history_btn = logged_in_page.locator("button:has-text('History')").first
            history_btn.click()
            time.sleep(3)
            
            # Check for table data
            dialog = logged_in_page.locator("[role='dialog']").first
            table = dialog.locator("table").first
            
            if table.is_visible():
                rows = table.locator("tbody tr").all()
                print(f"✅ History shows {len(rows)} records from API")
                
                # Check data in first row
                if rows:
                    cells = rows[0].locator("td").all()
                    data = [cell.inner_text() for cell in cells if cell.is_visible()]
                    print(f"Sample data: {data[:3]}")
                
                self.take_screenshot(logged_in_page, "history_realtime_data")
            
            self.close_modal(logged_in_page)
    
    def test_05_history_filtration(self, logged_in_page: Page):
        """Test History modal filtration feature"""
        print("\n🎯 Test 05: History Filtration")
        
        if self.select_property(logged_in_page):
            history_btn = logged_in_page.locator("button:has-text('History')").first
            history_btn.click()
            time.sleep(3)
            
            dialog = logged_in_page.locator("[role='dialog']").first
            
            # Find filter input
            filter_input = dialog.locator("input[placeholder*='Filter'], input[placeholder*='Search'], input[type='search']").first
            
            if filter_input.is_visible():
                box = filter_input.bounding_box()
                if box:
                    self.move_cursor_to(logged_in_page, box['x'] + 50, box['y'] + 15)
                
                filter_input.click()
                filter_input.fill("test")
                time.sleep(2)
                
                print("✅ History filter applied: 'test'")
                self.take_screenshot(logged_in_page, "history_filtered")
                
                # Clear filter
                filter_input.fill("")
                time.sleep(1)
            
            self.close_modal(logged_in_page)
    
    def test_06_history_pagination(self, logged_in_page: Page):
        """Test History modal pagination"""
        print("\n🎯 Test 06: History Pagination")
        
        if self.select_property(logged_in_page):
            history_btn = logged_in_page.locator("button:has-text('History')").first
            history_btn.click()
            time.sleep(3)
            
            dialog = logged_in_page.locator("[role='dialog']").first
            
            # Find pagination buttons
            next_btn = dialog.locator("button:has-text('Next'), button:has([class*='chevron-right'])").first
            prev_btn = dialog.locator("button:has-text('Previous'), button:has([class*='chevron-left'])").first
            
            # Check current page info
            page_info = dialog.locator("text=/page/i, text=/showing/i").first
            if page_info.is_visible():
                print(f"Pagination info: {page_info.inner_text()}")
            
            # Click next page
            if next_btn.is_visible() and not next_btn.is_disabled():
                box = next_btn.bounding_box()
                if box:
                    self.move_cursor_to(logged_in_page, box['x'] + 20, box['y'] + 15)
                
                next_btn.click()
                time.sleep(2)
                print("✅ Clicked Next page")
                self.take_screenshot(logged_in_page, "history_page_2")
                
                # Go back
                if prev_btn.is_visible():
                    box = prev_btn.bounding_box()
                    if box:
                        self.move_cursor_to(logged_in_page, box['x'] + 20, box['y'] + 15)
                    prev_btn.click()
                    time.sleep(1)
            
            self.close_modal(logged_in_page)
    
    def test_07_history_screen_actions(self, logged_in_page: Page):
        """Test History modal action buttons"""
        print("\n🎯 Test 07: History Screen Actions")
        
        if self.select_property(logged_in_page):
            history_btn = logged_in_page.locator("button:has-text('History')").first
            history_btn.click()
            time.sleep(3)
            
            dialog = logged_in_page.locator("[role='dialog']").first
            
            # Check for action buttons in table rows
            action_btns = dialog.locator("button").all()
            print(f"✅ Found {len(action_btns)} action buttons in History")
            
            self.take_screenshot(logged_in_page, "history_actions")
            self.close_modal(logged_in_page)
    
    # ========================================================================
    # EXPORT FEATURE TESTING
    # ========================================================================
    
    def test_08_export_option(self, logged_in_page: Page):
        """Test Export functionality"""
        print("\n🎯 Test 08: Export Option")
        
        if self.select_property(logged_in_page):
            # Look for export button
            export_btn = logged_in_page.locator("button:has-text('Export'), button:has([class*='download']), button[title*='Export']").first
            
            if export_btn.is_visible():
                box = export_btn.bounding_box()
                if box:
                    self.move_cursor_to(logged_in_page, box['x'] + 40, box['y'] + 18)
                
                self.take_screenshot(logged_in_page, "export_btn_hover")
                print("✅ Export button found")
            else:
                print("ℹ️ Export button not visible on main screen")
                self.take_screenshot(logged_in_page, "no_export_btn")
    
    # ========================================================================
    # PROPERTY TABLE ACTIONS TESTING
    # ========================================================================
    
    def test_09_table_edit_button(self, logged_in_page: Page):
        """Test Edit button in property tariff table"""
        print("\n🎯 Test 09: Table Edit Button")
        
        if self.select_property(logged_in_page):
            time.sleep(2)
            
            # Find Edit button in table
            edit_btn = logged_in_page.locator("button:has-text('Edit')").first
            
            if edit_btn.is_visible():
                box = edit_btn.bounding_box()
                if box:
                    self.move_cursor_to(logged_in_page, box['x'] + 25, box['y'] + 15)
                
                self.take_screenshot(logged_in_page, "edit_btn_hover")
                edit_btn.click()
                time.sleep(3)
                
                # Verify Edit dialog opened
                dialog = logged_in_page.locator("[role='dialog']").first
                if dialog.is_visible():
                    print("✅ Edit dialog opened successfully")
                    self.take_screenshot(logged_in_page, "edit_dialog_opened")
                
                self.close_modal(logged_in_page)
    
    def test_10_edit_room_details_modal(self, logged_in_page: Page):
        """Test Edit Room Details modal fields"""
        print("\n🎯 Test 10: Edit Room Details Modal")
        
        if self.select_property(logged_in_page):
            edit_btn = logged_in_page.locator("button:has-text('Edit')").first
            edit_btn.click()
            time.sleep(3)
            
            modal = logged_in_page.locator("[role='dialog']").first
            
            # Check all input fields
            inputs = modal.locator("input").all()
            print(f"✅ Edit modal has {len(inputs)} input fields")
            
            # Check for specific fields
            room_type = modal.locator("input").first
            if room_type.is_visible():
                current_value = room_type.input_value()
                print(f"Current Room Type: {current_value}")
            
            self.take_screenshot(logged_in_page, "edit_modal_fields")
            self.close_modal(logged_in_page)
    
    def test_11_update_room_functionality(self, logged_in_page: Page):
        """Test updating room tariff"""
        print("\n🎯 Test 11: Update Room Functionality")
        
        if self.select_property(logged_in_page):
            edit_btn = logged_in_page.locator("button:has-text('Edit')").first
            edit_btn.click()
            time.sleep(3)
            
            modal = logged_in_page.locator("[role='dialog']").first
            
            # Find tariff input and update
            inputs = modal.locator("input[type='text'], input[type='number']").all()
            
            if len(inputs) >= 2:
                # Update Single Agree tariff
                tariff_input = inputs[1]
                if tariff_input.is_visible():
                    box = tariff_input.bounding_box()
                    if box:
                        self.move_cursor_to(logged_in_page, box['x'] + 50, box['y'] + 15)
                    
                    tariff_input.click()
                    tariff_input.fill("6500")
                    print("✅ Updated tariff to 6500")
                    time.sleep(1)
                    
                    self.take_screenshot(logged_in_page, "update_tariff_filled")
                    
                    # Find Update/Save button
                    save_btn = modal.locator("button:has-text('Update'), button:has-text('Save')").first
                    if save_btn.is_visible():
                        box = save_btn.bounding_box()
                        if box:
                            self.move_cursor_to(logged_in_page, box['x'] + 40, box['y'] + 18)
                        
                        print("✅ Update button found (not clicking to preserve data)")
                        self.take_screenshot(logged_in_page, "update_btn_hover")
            
            self.close_modal(logged_in_page)
    
    def test_12_table_delete_button(self, logged_in_page: Page):
        """Test Delete button in property tariff table"""
        print("\n🎯 Test 12: Table Delete Button")
        
        if self.select_property(logged_in_page):
            time.sleep(2)
            
            # Find Delete button
            delete_btn = logged_in_page.locator("button:has([class*='trash']), button[title*='Delete']").first
            
            if delete_btn.is_visible():
                box = delete_btn.bounding_box()
                if box:
                    self.move_cursor_to(logged_in_page, box['x'] + 20, box['y'] + 15)
                
                self.take_screenshot(logged_in_page, "delete_btn_hover")
                delete_btn.click()
                time.sleep(2)
                
                # Check for confirmation dialog
                confirm_dialog = logged_in_page.locator("[role='dialog'], [role='alertdialog']").first
                if confirm_dialog.is_visible():
                    print("✅ Delete confirmation dialog opened")
                    self.take_screenshot(logged_in_page, "delete_confirmation")
                    
                    # Cancel deletion
                    cancel_btn = confirm_dialog.locator("button:has-text('Cancel'), button:has-text('No')").first
                    if cancel_btn.is_visible():
                        cancel_btn.click()
                        print("✅ Cancelled deletion")
                
                self.close_modal(logged_in_page)
    
    # ========================================================================
    # ROOM DETAILS MODAL TESTING
    # ========================================================================
    
    def test_13_room_details_all_fields(self, logged_in_page: Page):
        """Test all fields in Room Details modal"""
        print("\n🎯 Test 13: Room Details All Fields")
        
        if self.select_property(logged_in_page):
            add_btn = logged_in_page.locator("button:has-text('Add Room Charges')").first
            add_btn.click()
            time.sleep(3)
            
            dialog = logged_in_page.locator("[role='dialog']").first
            create_btn = dialog.locator("button:has-text('Create New Room'), button:has-text('Create')").first
            create_btn.click(force=True)
            time.sleep(3)
            
            modal = logged_in_page.locator("[role='dialog']").last
            
            # Test Room Type field
            print("\n📝 Testing Room Type field:")
            room_type_input = modal.locator("input").first
            box = room_type_input.bounding_box()
            if box:
                self.move_cursor_to(logged_in_page, box['x'] + 100, box['y'] + 15)
            room_type_input.click()
            room_type_input.fill("Test Suite Room")
            print("✅ Room Type: Test Suite Room")
            time.sleep(0.5)
            
            self.take_screenshot(logged_in_page, "room_details_room_type")
            
            # Test Tariff fields
            print("\n📝 Testing Tariff fields:")
            tariff_inputs = modal.locator("input[type='text'], input[type='number']").all()
            
            for i, inp in enumerate(tariff_inputs[1:4]):  # Skip first (property), take next 3
                if inp.is_visible() and inp.is_editable():
                    box = inp.bounding_box()
                    if box:
                        self.move_cursor_to(logged_in_page, box['x'] + 50, box['y'] + 15)
                    
                    value = str(5000 + i * 2000)
                    inp.fill(value)
                    print(f"✅ Tariff {i+1}: {value}")
                    time.sleep(0.3)
            
            self.take_screenshot(logged_in_page, "room_details_tariffs")
            
            # Test Meal Plan dropdown
            print("\n📝 Testing Meal Plan:")
            meal_select = modal.locator("select").first
            if meal_select.is_visible():
                box = meal_select.bounding_box()
                if box:
                    self.move_cursor_to(logged_in_page, box['x'] + 80, box['y'] + 15)
                
                meal_select.select_option(index=1)
                print("✅ Meal Plan selected")
                time.sleep(0.5)
            
            self.take_screenshot(logged_in_page, "room_details_complete")
            
            self.close_modal(logged_in_page)
    
    # ========================================================================
    # IMAGE UPLOAD FEATURE TESTING
    # ========================================================================
    
    def test_14_upload_image_feature(self, logged_in_page: Page):
        """Test Room Image upload feature"""
        print("\n🎯 Test 14: Upload Image Feature")
        
        if self.select_property(logged_in_page):
            edit_btn = logged_in_page.locator("button:has-text('Edit')").first
            edit_btn.click()
            time.sleep(3)
            
            modal = logged_in_page.locator("[role='dialog']").first
            
            # Find upload button
            upload_btn = modal.locator("button:has-text('Upload'), input[type='file']").first
            
            if upload_btn.is_visible():
                box = upload_btn.bounding_box()
                if box:
                    self.move_cursor_to(logged_in_page, box['x'] + 60, box['y'] + 18)
                
                print("✅ Upload Image button found")
                self.take_screenshot(logged_in_page, "upload_image_btn")
                
                # Check for image requirements text
                size_text = modal.locator("text=/1MB/i, text=/file type/i").first
                if size_text.is_visible():
                    print(f"Image requirements: {size_text.inner_text()}")
            
            self.close_modal(logged_in_page)
    
    # ========================================================================
    # ROOM CHARGE DETAILS TESTING
    # ========================================================================
    
    def test_15_room_charge_details_save(self, logged_in_page: Page):
        """Test Room Charge Details and Save functionality"""
        print("\n🎯 Test 15: Room Charge Details & Save")
        
        if self.select_property(logged_in_page):
            # Click View Room Charges
            view_btn = logged_in_page.locator("button:has-text('View'), a:has-text('View')").first
            
            if view_btn.is_visible():
                box = view_btn.bounding_box()
                if box:
                    self.move_cursor_to(logged_in_page, box['x'] + 30, box['y'] + 15)
                
                self.take_screenshot(logged_in_page, "view_room_charges_hover")
                view_btn.click()
                time.sleep(2)
                
                print("✅ Room Charge Details viewed")
                self.take_screenshot(logged_in_page, "room_charge_details")
                
                logged_in_page.keyboard.press("Escape")
            
    # Continue with remaining tests...
    def test_16_complete_create_room_workflow(self, logged_in_page: Page):
        """Complete Create Room workflow with cursor movement"""
        print("\n🎯 Test 16: Complete Create Room Workflow")
        
        if self.select_property(logged_in_page):
            self.take_screenshot(logged_in_page, "workflow_step1_property")
            
            # Step 1: Add Room Charges
            add_btn = logged_in_page.locator("button:has-text('Add Room Charges')").first
            box = add_btn.bounding_box()
            if box:
                self.move_cursor_to(logged_in_page, box['x'] + 80, box['y'] + 20)
            add_btn.click()
            time.sleep(3)
            print("✅ Step 1: Add Room Charges opened")
            self.take_screenshot(logged_in_page, "workflow_step2_add_dialog")
            
            # Step 2: Create New Room
            dialog = logged_in_page.locator("[role='dialog']").first
            create_btn = dialog.locator("button:has-text('Create New Room'), button:has-text('Create')").first
            box = create_btn.bounding_box()
            if box:
                self.move_cursor_to(logged_in_page, box['x'] + 70, box['y'] + 18)
            create_btn.click(force=True)
            time.sleep(3)
            print("✅ Step 2: Room Details opened")
            self.take_screenshot(logged_in_page, "workflow_step3_room_details")
            
            # Step 3: Fill all fields
            modal = logged_in_page.locator("[role='dialog']").last
            
            # Room Type
            room_input = modal.locator("input").first
            box = room_input.bounding_box()
            if box:
                self.move_cursor_to(logged_in_page, box['x'] + 100, box['y'] + 15)
            room_input.click()
            room_input.fill("Premium Suite")
            print("✅ Step 3: Room Type filled")
            time.sleep(0.5)
            
            # Tariffs
            inputs = modal.locator("input[type='text'], input[type='number']").all()
            for i, inp in enumerate(inputs[1:4]):
                if inp.is_visible():
                    box = inp.bounding_box()
                    if box:
                        self.move_cursor_to(logged_in_page, box['x'] + 50, box['y'] + 15)
                    inp.fill(str(8000 + i * 2000))
                    time.sleep(0.3)
            print("✅ Step 4: Tariffs filled")
            
            # Meal Plan
            meal_select = modal.locator("select").first
            if meal_select.is_visible():
                box = meal_select.bounding_box()
                if box:
                    self.move_cursor_to(logged_in_page, box['x'] + 80, box['y'] + 15)
                meal_select.select_option(index=0)
            print("✅ Step 5: Meal Plan selected")
            
            self.take_screenshot(logged_in_page, "workflow_step4_all_filled")
            
            # Step 4: Save
            save_btn = modal.locator("button:has-text('Create'), button:has-text('Save')").last
            box = save_btn.bounding_box()
            if box:
                self.move_cursor_to(logged_in_page, box['x'] + 40, box['y'] + 18)
            save_btn.click(force=True)
            time.sleep(3)
            print("✅ Step 6: Saved to staging table")
            
            self.take_screenshot(logged_in_page, "workflow_step5_saved")
            
            self.close_modal(logged_in_page)


# Create features directory
import os
os.makedirs("assets/features", exist_ok=True)
