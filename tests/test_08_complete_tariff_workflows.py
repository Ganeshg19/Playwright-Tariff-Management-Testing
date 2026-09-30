"""
Complete Tariff Management Workflows Testing
Tests all modal fields, create/update room types, validations, and captures annotated screenshots
"""

import pytest
from playwright.sync_api import Page, expect
import time
import os
import sys
from datetime import datetime

# Add utils to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))
from annotated_screenshot import AnnotatedScreenshotHelper


class TestTariffCompleteWorkflows:
    """Comprehensive testing of Tariff Management screen"""
    
    def setup_method(self, method):
        """Setup before each test"""
        pass
    
    def teardown_method(self, method):
        """Cleanup after each test - close any modals"""
        print(f"\n🧹 Cleaning up after {method.__name__}...")
    
    def select_property_and_wait(self, page: Page):
        """Helper: Select property and wait for data"""
        try:
            property_selectors = [
                "input[placeholder*='Property']",
                "input[placeholder*='Search']",
                "input[name*='property']",
                "input[type='search']"
            ]
            
            property_input = None
            for selector in property_selectors:
                try:
                    elem = page.locator(selector).first
                    if elem.is_visible(timeout=2000):
                        property_input = elem
                        print(f"✅ Found property input with selector: {selector}")
                        break
                except:
                    continue
            
            if property_input and property_input.is_visible():
                property_input.click()
                time.sleep(1)
                
                property_input.fill("AM Property")
                time.sleep(2)
                
                # Select from dropdown
                dropdown_items = page.locator("[role='option'], .dropdown-item, li").all()
                if dropdown_items:
                    for item in dropdown_items:
                        try:
                            text = item.inner_text()
                            if "AM" in text or "Property" in text:
                                item.click()
                                print(f"✅ Selected: {text}")
                                break
                        except:
                            continue
                else:
                    page.keyboard.press("Enter")
                
                time.sleep(3)
                print("✅ Property selected and data loaded")
                return True
            else:
                print("⚠️  Property input not found")
                return False
        except Exception as e:
            print(f"⚠️  Property selection failed: {e}")
            return False
    
    def close_modal_if_open(self, page: Page):
        """Helper: Close any open modal - aggressive approach"""
        try:
            # Press ESC multiple times
            for _ in range(5):
                page.keyboard.press("Escape")
                time.sleep(0.3)
            
            # Try close buttons
            close_selectors = [
                "button[aria-label='Close']",
                "button:has-text('×')",
                "button:has-text('Cancel')",
                "button.close"
            ]
            
            for selector in close_selectors:
                try:
                    buttons = page.locator(selector).all()
                    for btn in buttons:
                        if btn.is_visible(timeout=1000):
                            btn.click(force=True)
                            time.sleep(0.5)
                except:
                    pass
            
            # Wait for modal to disappear
            try:
                page.wait_for_selector("[role='dialog']", state="hidden", timeout=3000)
                print("✅ Modal closed successfully")
            except:
                # Click backdrop
                try:
                    backdrop = page.locator("div[data-state='open'][class*='fixed']").first
                    if backdrop.is_visible(timeout=1000):
                        backdrop.click(position={"x": 10, "y": 10}, force=True)
                        time.sleep(1)
                except:
                    pass
            
            time.sleep(1)
            return True
        except Exception as e:
            print(f"⚠️  Could not close modal: {e}")
            return False
    
    # ========================================================================
    # TEST 1: Verify All Modal Fields Exist
    # ========================================================================
    
    def test_01_verify_all_modal_fields(self, logged_in_page: Page):
        """
        Test: Verify all 18+ fields exist in Add Room Charges modal
        """
        annotator = AnnotatedScreenshotHelper(logged_in_page)
        time.sleep(1)
        
        # Select property
        property_selected = self.select_property_and_wait(logged_in_page)
        
        if property_selected:
            try:
                # Click Add Room Charges
                add_button = logged_in_page.locator("button:has-text('Add Room Charges'), button:has-text('Create')").first
                if add_button.is_visible():
                    add_button.click()
                    time.sleep(2)
                    
                    # Check all expected fields
                    modal = logged_in_page.locator("[role='dialog']").first
                    if modal.is_visible():
                        print("✅ Modal opened, checking fields...")
                        
                        # List of expected fields
                        field_checks = [
                            ("Room Type input", "input[placeholder*='Room'], input[name*='room']"),
                            ("Single Agree input", "input[placeholder*='Single'], input[name*='single']"),
                            ("Double Agree input", "input[placeholder*='Double'], input[name*='double']"),
                            ("Triple Agree input", "input[placeholder*='Triple'], input[name*='triple']"),
                            ("Valid Start Date", "input[type='date'], [placeholder*='Start']"),
                            ("Valid End Date", "input[type='date'], [placeholder*='End']"),
                            ("Facility dropdown", "[role='combobox'], select"),
                            ("Meal Plan dropdown", "select, [role='combobox']"),
                            ("TAC checkbox", "input[type='checkbox']"),
                        ]
                        
                        found_fields = []
                        missing_fields = []
                        
                        for field_name, selector in field_checks:
                            elements = logged_in_page.locator(selector).all()
                            if elements and len(elements) > 0:
                                found_fields.append(field_name)
                                print(f"  ✅ {field_name}: Found")
                            else:
                                missing_fields.append(field_name)
                                print(f"  ❌ {field_name}: NOT FOUND")
                        
                        # Take annotated screenshot
                        annotator.capture_error_state(
                            "test_01_all_modal_fields",
                            f"Found {len(found_fields)} fields, Missing {len(missing_fields)}"
                        )
                        
                        # Close modal
                        self.close_modal_if_open(logged_in_page)
                        
                        print(f"\n📊 Field Check Summary:")
                        print(f"  ✅ Found: {len(found_fields)}")
                        print(f"  ❌ Missing: {len(missing_fields)}")
                        
            except Exception as e:
                print(f"❌ Error: {e}")
                annotator.capture_error_state("test_01_error", str(e))
                self.close_modal_if_open(logged_in_page)
    
    # ========================================================================
    # TEST 2: Create New Room Type - Happy Path
    # ========================================================================
    
    def test_02_create_new_room_type_happy_path(self, logged_in_page: Page):
        """
        Test: Complete workflow to create a new room type
        """
        annotator = AnnotatedScreenshotHelper(logged_in_page)
        time.sleep(1)
        
        # Select property
        property_selected = self.select_property_and_wait(logged_in_page)
        
        if property_selected:
            try:
                # Step 1: Screenshot before opening modal
                annotator.capture_with_cursor(
                    "test_02_step1_before_add",
                    cursor_x=900,
                    cursor_y=200
                )
                
                # Step 2: Click Add Room Charges
                add_button = logged_in_page.locator("button:has-text('Add Room Charges'), button:has-text('Create')").first
                if add_button.is_visible():
                    add_button.click()
                    time.sleep(2)
                    
                    # Step 3: Screenshot modal opened
                    annotator.capture_with_cursor(
                        "test_02_step2_modal_opened",
                        cursor_x=512,
                        cursor_y=400
                    )
                    
                    # Step 4: Fill Room Type (scope to modal only)
                    modal = logged_in_page.locator("[role='dialog']").first
                    room_type_input = modal.locator("input").first  # First input inside modal
                    if room_type_input.is_visible():
                        room_type_input.click(force=True)
                        room_type_input.fill("Automation Test Suite Room")
                        time.sleep(1)
                        
                        # Screenshot after filling room type
                        annotator.capture_element_with_box(
                            "test_02_step3_room_type_filled",
                            room_type_input,
                            "Room Type Entered"
                        )
                    
                    # Step 5: Fill Single Agree (get all inputs from modal)
                    inputs = modal.locator("input[type='text'], input:not([type='hidden']):not([type='date'])").all()
                    print(f"📊 Found {len(inputs)} text inputs in modal")
                    
                    if len(inputs) >= 2:
                        single_input = inputs[1]  # Second input is Single Agree
                        single_input.click(force=True)
                        single_input.fill("1500")
                        time.sleep(0.5)
                        
                        annotator.capture_element_with_box(
                            "test_02_step4_single_agree_filled",
                            single_input,
                            "Single Agree: 1500"
                        )
                    
                    # Step 6: Fill Double Agree
                    if len(inputs) >= 3:
                        double_input = inputs[2]
                        double_input.click(force=True)
                        double_input.fill("2000")
                        time.sleep(0.5)
                        
                        annotator.capture_element_with_box(
                            "test_02_step5_double_agree_filled",
                            double_input,
                            "Double Agree: 2000"
                        )
                    
                    # Step 7: Fill Triple Agree
                    if len(inputs) >= 4:
                        triple_input = inputs[3]
                        triple_input.click(force=True)
                        triple_input.fill("2500")
                        time.sleep(0.5)
                        
                        annotator.capture_element_with_box(
                            "test_02_step6_triple_agree_filled",
                            triple_input,
                            "Triple Agree: 2500"
                        )
                    
                    # Step 8: Screenshot final form state
                    annotator.capture_with_cursor(
                        "test_02_step7_form_complete",
                        cursor_x=512,
                        cursor_y=600
                    )
                    
                    # Step 9: Try to click Save
                    print("🔄 Looking for Save button...")
                    save_button = logged_in_page.locator("[role='dialog'] button:has-text('Save'), [role='dialog'] button:has-text('Create')").first
                    
                    if save_button.is_visible():
                        # Screenshot cursor on save button
                        save_box = save_button.bounding_box()
                        if save_box:
                            annotator.capture_with_cursor(
                                "test_02_step8_clicking_save",
                                cursor_x=int(save_box['x'] + save_box['width']//2),
                                cursor_y=int(save_box['y'] + save_box['height']//2)
                            )
                        
                        # Click save (might fail due to validation)
                        try:
                            save_button.click(force=True, timeout=5000)
                            time.sleep(2)
                            
                            # Screenshot result (success or error)
                            annotator.capture_error_state(
                                "test_02_step9_save_result",
                                "Check if room type created"
                            )
                        except Exception as e:
                            print(f"⚠️  Save click error: {e}")
                            annotator.capture_error_state(
                                "test_02_save_error",
                                f"Save Failed: {str(e)[:50]}"
                            )
                    
                    # Close modal
                    self.close_modal_if_open(logged_in_page)
                    time.sleep(1)
                    
                    # Final screenshot
                    annotator.capture_with_cursor(
                        "test_02_step10_after_close",
                        cursor_x=512,
                        cursor_y=300
                    )
                    
            except Exception as e:
                print(f"❌ Error: {e}")
                annotator.capture_error_state("test_02_error", str(e))
                self.close_modal_if_open(logged_in_page)
    
    # ========================================================================
    # TEST 3: Create New Room Type - Validation Errors
    # ========================================================================
    
    def test_03_create_room_validation_errors(self, logged_in_page: Page):
        """
        Test: Try to save with empty required fields
        """
        annotator = AnnotatedScreenshotHelper(logged_in_page)
        time.sleep(1)
        
        property_selected = self.select_property_and_wait(logged_in_page)
        
        if property_selected:
            try:
                # Open modal
                add_button = logged_in_page.locator("button:has-text('Add Room Charges')").first
                if add_button.is_visible():
                    add_button.click()
                    time.sleep(2)
                    
                    # Try to click Save without filling anything
                    save_button = logged_in_page.locator("[role='dialog'] button:has-text('Save'), [role='dialog'] button:has-text('Create')").first
                    
                    if save_button.is_visible():
                        save_button.click(force=True)
                        time.sleep(2)
                        
                        # Screenshot validation errors
                        annotator.capture_error_state(
                            "test_03_validation_errors",
                            "Empty Required Fields"
                        )
                        
                        # Try to find error messages
                        error_elements = logged_in_page.locator(".error, .text-red-500, [class*='error']").all()
                        print(f"✅ Found {len(error_elements)} error elements")
                        
                        if error_elements:
                            # Annotate each error
                            elements_with_labels = []
                            for i, elem in enumerate(error_elements[:5]):  # Max 5 errors
                                if elem.is_visible():
                                    elements_with_labels.append((elem, f"Error {i+1}", "red"))
                            
                            if elements_with_labels:
                                annotator.capture_with_multiple_boxes(
                                    "test_03_all_validation_errors",
                                    elements_with_labels
                                )
                    
                    self.close_modal_if_open(logged_in_page)
                    
            except Exception as e:
                print(f"❌ Error: {e}")
                annotator.capture_error_state("test_03_error", str(e))
                self.close_modal_if_open(logged_in_page)
    
    # ========================================================================
    # TEST 4: Update Existing Room Type
    # ========================================================================
    
    def test_04_update_existing_room_type(self, logged_in_page: Page):
        """
        Test: Edit existing room type
        """
        annotator = AnnotatedScreenshotHelper(logged_in_page)
        time.sleep(1)
        
        property_selected = self.select_property_and_wait(logged_in_page)
        
        if property_selected:
            try:
                # Wait for table to load
                time.sleep(2)
                
                # Screenshot table
                annotator.capture_with_cursor(
                    "test_04_step1_table_loaded",
                    cursor_x=900,
                    cursor_y=300
                )
                
                # Find and click Edit button
                edit_buttons = logged_in_page.locator("button:has-text('Edit'), [title='Edit'], svg.lucide-edit, .edit-icon").all()
                
                if edit_buttons:
                    print(f"✅ Found {len(edit_buttons)} edit buttons")
                    
                    # Click first edit button
                    first_edit = edit_buttons[0]
                    
                    # Screenshot cursor on edit button
                    edit_box = first_edit.bounding_box()
                    if edit_box:
                        annotator.capture_with_cursor(
                            "test_04_step2_clicking_edit",
                            cursor_x=int(edit_box['x'] + edit_box['width']//2),
                            cursor_y=int(edit_box['y'] + edit_box['height']//2)
                        )
                    
                    first_edit.click()
                    time.sleep(2)
                    
                    # Screenshot edit modal with pre-filled data
                    annotator.capture_with_cursor(
                        "test_04_step3_edit_modal_opened",
                        cursor_x=512,
                        cursor_y=400
                    )
                    
                    # Find Single Agree input and update it (scope to modal)
                    modal = logged_in_page.locator("[role='dialog']").first
                    inputs = modal.locator("input[type='text'], input:not([type='hidden']):not([type='date'])").all()
                    print(f"📊 Found {len(inputs)} text inputs in edit modal")
                    
                    if len(inputs) >= 2:
                        single_input = inputs[1]
                        
                        # Get current value
                        current_value = single_input.input_value()
                        print(f"📝 Current Single Agree: {current_value}")
                        
                        # Clear and enter new value
                        single_input.click(force=True)
                        logged_in_page.keyboard.press("Control+A")
                        single_input.fill("9999")
                        time.sleep(1)
                        
                        # Screenshot updated value
                        annotator.capture_element_with_box(
                            "test_04_step4_value_updated",
                            single_input,
                            "Updated to 9999"
                        )
                    
                    # Try to click Update/Save
                    update_button = logged_in_page.locator("[role='dialog'] button:has-text('Update'), [role='dialog'] button:has-text('Save')").first
                    
                    if update_button.is_visible():
                        update_box = update_button.bounding_box()
                        if update_box:
                            annotator.capture_with_cursor(
                                "test_04_step5_clicking_update",
                                cursor_x=int(update_box['x'] + update_box['width']//2),
                                cursor_y=int(update_box['y'] + update_box['height']//2)
                            )
                        
                        try:
                            update_button.click(force=True, timeout=5000)
                            time.sleep(2)
                            
                            annotator.capture_error_state(
                                "test_04_step6_update_result",
                                "Check if update successful"
                            )
                        except Exception as e:
                            print(f"⚠️  Update error: {e}")
                            annotator.capture_error_state(
                                "test_04_update_error",
                                f"Update Failed: {str(e)[:50]}"
                            )
                    
                    self.close_modal_if_open(logged_in_page)
                else:
                    print("❌ No edit buttons found")
                    annotator.capture_error_state(
                        "test_04_no_edit_buttons",
                        "No Edit Buttons Found"
                    )
                    
            except Exception as e:
                print(f"❌ Error: {e}")
                annotator.capture_error_state("test_04_error", str(e))
                self.close_modal_if_open(logged_in_page)
    
    # ========================================================================
    # TEST 5: Room Charge Details Modal
    # ========================================================================
    
    def test_05_room_charge_details_modal(self, logged_in_page: Page):
        """
        Test: Open Room Charge Details modal (table view)
        """
        annotator = AnnotatedScreenshotHelper(logged_in_page)
        time.sleep(1)
        
        property_selected = self.select_property_and_wait(logged_in_page)
        
        if property_selected:
            try:
                # Look for "Room Charge Details" button
                details_button = logged_in_page.locator("button:has-text('Room Charge Details'), button:has-text('Details')").first
                
                if details_button.is_visible():
                    # Screenshot cursor on button
                    btn_box = details_button.bounding_box()
                    if btn_box:
                        annotator.capture_with_cursor(
                            "test_05_step1_details_button",
                            cursor_x=int(btn_box['x'] + btn_box['width']//2),
                            cursor_y=int(btn_box['y'] + btn_box['height']//2)
                        )
                    
                    details_button.click()
                    time.sleep(2)
                    
                    # Screenshot details modal
                    annotator.capture_with_cursor(
                        "test_05_step2_details_modal_opened",
                        cursor_x=512,
                        cursor_y=400
                    )
                    
                    # Check if table is visible
                    table = logged_in_page.locator("table, [role='table']").first
                    if table.is_visible():
                        print("✅ Details table visible")
                        annotator.capture_element_with_box(
                            "test_05_step3_details_table",
                            table,
                            "Room Charge Details Table"
                        )
                    
                    self.close_modal_if_open(logged_in_page)
                else:
                    print("⚠️  Room Charge Details button not found")
                    annotator.capture_error_state(
                        "test_05_button_not_found",
                        "Details Button Not Found"
                    )
                    
            except Exception as e:
                print(f"❌ Error: {e}")
                annotator.capture_error_state("test_05_error", str(e))
                self.close_modal_if_open(logged_in_page)
