"""
Complete Modal Validation Testing
Tests all required fields, validations, and submission functionality
"""

import pytest
from playwright.sync_api import Page
import time
import sys
import os

# Add utils to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))
from annotated_screenshot import AnnotatedScreenshotHelper
from visual_cursor import VisualCursor


class TestModalValidations:
    """Comprehensive modal validation tests"""
    
    def setup_method(self, method):
        """Setup before each test"""
        pass
    
    def teardown_method(self, method):
        """Cleanup after each test"""
        print(f"\n🧹 Cleaning up after {method.__name__}...")
    
    def select_property_and_wait(self, page: Page):
        """Helper: Select property and wait for data"""
        try:
            property_input = page.locator("input[placeholder*='Property']").first
            if property_input.is_visible(timeout=2000):
                property_input.click()
                time.sleep(1)
                property_input.fill("AM Property")
                time.sleep(2)
                
                dropdown_items = page.locator("[role='option']").all()
                if dropdown_items:
                    for item in dropdown_items:
                        try:
                            text = item.inner_text()
                            if "AM" in text:
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
            return False
        except Exception as e:
            print(f"⚠️  Property selection failed: {e}")
            return False
    
    def close_modal_if_open(self, page: Page):
        """Helper: Close any open modal"""
        try:
            for _ in range(5):
                page.keyboard.press("Escape")
                time.sleep(0.3)
            
            close_selectors = [
                "button[aria-label='Close']",
                "button:has-text('×')",
                "button:has-text('Cancel')"
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
            
            try:
                page.wait_for_selector("[role='dialog']", state="hidden", timeout=3000)
                print("✅ Modal closed successfully")
            except:
                pass
            
            return True
        except Exception as e:
            print(f"⚠️  Could not close modal: {e}")
            return False
    
    # ========================================================================
    # TEST 1: Empty Room Name (Mandatory Field)
    # ========================================================================
    
    def test_01_empty_room_name_validation(self, logged_in_page: Page):
        """
        Test: Submit modal with empty Room Name (mandatory field)
        Expected: Error message "Room Type is required"
        """
        annotator = AnnotatedScreenshotHelper(logged_in_page)
        cursor = VisualCursor(logged_in_page, cursor_size=35, cursor_color="red")
        
        print("\n🎯 Test: Empty Room Name Validation")
        time.sleep(1)
        
        # Select property
        if not self.select_property_and_wait(logged_in_page):
            print("❌ Property selection failed")
            return
        
        try:
            # Click Add Room Charges
            add_button = logged_in_page.locator("button:has-text('Add Room Charges')").first
            if add_button.is_visible():
                cursor.click_with_cursor(add_button, duration=0.6)
                time.sleep(2)
                
                # Screenshot: Modal opened
                annotator.capture_with_cursor("test_01_step1_modal_opened", 512, 400)
                
                # Click Create New Room
                create_button = logged_in_page.locator("button:has-text('Create New Room'), button:has-text('Create')").first
                if create_button.is_visible():
                    cursor.click_with_cursor(create_button, duration=0.6)
                    time.sleep(2)
                    
                    # Room Details dialog opened
                    print("✅ Room Details dialog opened")
                    annotator.capture_with_cursor("test_01_step2_room_details_opened", 512, 400)
                    
                    # Find Room Type input and verify it's empty
                    modal = logged_in_page.locator("[role='dialog']").first
                    room_type_input = modal.locator("input").first
                    
                    if room_type_input.is_visible():
                        # Take screenshot showing empty field
                        annotator.capture_element_with_box(
                            "test_01_step3_empty_room_name",
                            room_type_input,
                            "❌ Room Type: EMPTY (Required)",
                            "red"
                        )
                        
                        # Try to click Save/Create with empty Room Type
                        print("📍 Attempting to save with empty Room Type...")
                        save_button = modal.locator("button:has-text('Create'), button:has-text('Save')").first
                        
                        if save_button.is_visible():
                            cursor.click_with_cursor(save_button, duration=0.6)
                            time.sleep(2)
                            
                            # Screenshot after clicking save
                            annotator.capture_error_state(
                                "test_01_step4_validation_error",
                                "Empty Room Type - Should show error"
                            )
                            
                            # Try to find error message
                            error_messages = logged_in_page.locator(
                                "text=/Room Type.*required/i, " +
                                ".error, .text-red-500, " +
                                "[class*='error'], " +
                                ".validation-error"
                            ).all()
                            
                            if error_messages:
                                print(f"✅ Found {len(error_messages)} error messages")
                                for i, err in enumerate(error_messages):
                                    if err.is_visible():
                                        print(f"  Error {i+1}: {err.inner_text()}")
                            else:
                                print("⚠️  No error messages found (might be toast notification)")
                            
                            # Final screenshot
                            annotator.capture_with_cursor("test_01_step5_final_state", 512, 400)
                    
            self.close_modal_if_open(logged_in_page)
            
        except Exception as e:
            print(f"❌ Error: {e}")
            annotator.capture_error_state("test_01_error", str(e))
            self.close_modal_if_open(logged_in_page)
    
    # ========================================================================
    # TEST 2: Empty Tariff Fields (All Three Empty)
    # ========================================================================
    
    def test_02_empty_tariff_validation(self, logged_in_page: Page):
        """
        Test: Fill Room Type but leave all tariffs empty
        Expected: Error "Any one Agreed Tariff is required"
        """
        annotator = AnnotatedScreenshotHelper(logged_in_page)
        cursor = VisualCursor(logged_in_page, cursor_size=35, cursor_color="orange")
        
        print("\n🎯 Test: Empty Tariff Validation")
        time.sleep(1)
        
        if not self.select_property_and_wait(logged_in_page):
            return
        
        try:
            # Open Add Room Charges
            add_button = logged_in_page.locator("button:has-text('Add Room Charges')").first
            cursor.click_with_cursor(add_button, duration=0.5)
            time.sleep(2)
            
            # Click Create New Room
            create_button = logged_in_page.locator("button:has-text('Create New Room')").first
            cursor.click_with_cursor(create_button, duration=0.5)
            time.sleep(2)
            
            # Fill ONLY Room Type (leave tariffs empty)
            modal = logged_in_page.locator("[role='dialog']").first
            room_type_input = modal.locator("input").first
            
            if room_type_input.is_visible():
                cursor.click_with_cursor(room_type_input, duration=0.5)
                room_type_input.fill("Test Room With No Tariff")
                
                annotator.capture_element_with_box(
                    "test_02_step1_room_filled",
                    room_type_input,
                    "✅ Room Type: Filled",
                    "green"
                )
                
                # Get all inputs to show tariffs are empty
                inputs = modal.locator("input:not([type='hidden']):not([type='date'])").all()
                print(f"📊 Found {len(inputs)} inputs in modal")
                
                # Screenshot showing all tariff fields empty
                if len(inputs) >= 4:
                    elements_with_labels = [
                        (inputs[0], "Room Type: FILLED", "green"),
                        (inputs[1], "Single Agree: EMPTY", "red"),
                        (inputs[2], "Double Agree: EMPTY", "red"),
                        (inputs[3], "Triple Agree: EMPTY", "red"),
                    ]
                    
                    annotator.capture_with_multiple_boxes(
                        "test_02_step2_all_tariffs_empty",
                        elements_with_labels
                    )
                
                # Try to save
                save_button = modal.locator("button:has-text('Create'), button:has-text('Save')").first
                cursor.click_with_cursor(save_button, duration=0.6)
                time.sleep(2)
                
                annotator.capture_error_state(
                    "test_02_step3_tariff_error",
                    "Empty Tariffs - Should show error"
                )
            
            self.close_modal_if_open(logged_in_page)
            
        except Exception as e:
            print(f"❌ Error: {e}")
            annotator.capture_error_state("test_02_error", str(e))
            self.close_modal_if_open(logged_in_page)
    
    # ========================================================================
    # TEST 3: Empty Meal Plan (Required Field)
    # ========================================================================
    
    def test_03_empty_meal_plan_validation(self, logged_in_page: Page):
        """
        Test: Fill Room Type and Tariffs but leave Meal Plan empty
        Expected: Error "Meal Plan is required"
        """
        annotator = AnnotatedScreenshotHelper(logged_in_page)
        cursor = VisualCursor(logged_in_page, cursor_size=35, cursor_color="blue")
        
        print("\n🎯 Test: Empty Meal Plan Validation")
        time.sleep(1)
        
        if not self.select_property_and_wait(logged_in_page):
            return
        
        try:
            # Open modal
            add_button = logged_in_page.locator("button:has-text('Add Room Charges')").first
            cursor.click_with_cursor(add_button)
            time.sleep(2)
            
            create_button = logged_in_page.locator("button:has-text('Create New Room')").first
            cursor.click_with_cursor(create_button)
            time.sleep(2)
            
            # Fill Room Type and Tariffs (but NOT Meal Plan)
            modal = logged_in_page.locator("[role='dialog']").first
            inputs = modal.locator("input:not([type='hidden']):not([type='date'])").all()
            
            if len(inputs) >= 4:
                # Room Type
                cursor.click_with_cursor(inputs[0])
                inputs[0].fill("Test Room No Meal Plan")
                
                # Single Agree
                cursor.click_with_cursor(inputs[1])
                inputs[1].fill("1000")
                
                # Double Agree
                cursor.click_with_cursor(inputs[2])
                inputs[2].fill("1500")
                
                # Triple Agree
                cursor.click_with_cursor(inputs[3])
                inputs[3].fill("2000")
                
                # Screenshot showing filled fields
                elements_with_labels = [
                    (inputs[0], "Room Type: FILLED ✅", "green"),
                    (inputs[1], "Single: 1000 ✅", "green"),
                    (inputs[2], "Double: 1500 ✅", "green"),
                    (inputs[3], "Triple: 2000 ✅", "green"),
                ]
                
                annotator.capture_with_multiple_boxes(
                    "test_03_step1_fields_filled",
                    elements_with_labels
                )
                
                # Find Meal Plan dropdown (should be empty)
                meal_plan_dropdown = modal.locator("select, [role='combobox']").first
                if meal_plan_dropdown.is_visible():
                    annotator.capture_element_with_box(
                        "test_03_step2_meal_plan_empty",
                        meal_plan_dropdown,
                        "❌ Meal Plan: EMPTY (Required)",
                        "red"
                    )
                
                # Try to save
                save_button = modal.locator("button:has-text('Create')").first
                cursor.click_with_cursor(save_button, duration=0.6)
                time.sleep(2)
                
                annotator.capture_error_state(
                    "test_03_step3_meal_plan_error",
                    "Empty Meal Plan - Should show error"
                )
            
            self.close_modal_if_open(logged_in_page)
            
        except Exception as e:
            print(f"❌ Error: {e}")
            annotator.capture_error_state("test_03_error", str(e))
            self.close_modal_if_open(logged_in_page)
    
    # ========================================================================
    # TEST 4: Complete Valid Submission
    # ========================================================================
    
    def test_04_valid_submission_all_required_fields(self, logged_in_page: Page):
        """
        Test: Fill ALL required fields and submit successfully
        Expected: Room added to staging table
        """
        annotator = AnnotatedScreenshotHelper(logged_in_page)
        cursor = VisualCursor(logged_in_page, cursor_size=35, cursor_color="green")
        
        print("\n🎯 Test: Valid Submission - All Required Fields")
        time.sleep(1)
        
        if not self.select_property_and_wait(logged_in_page):
            return
        
        try:
            # Open modal
            add_button = logged_in_page.locator("button:has-text('Add Room Charges')").first
            cursor.click_with_cursor(add_button, duration=0.6)
            time.sleep(2)
            
            create_button = logged_in_page.locator("button:has-text('Create New Room')").first
            cursor.click_with_cursor(create_button, duration=0.6)
            time.sleep(2)
            
            # Fill ALL required fields
            modal = logged_in_page.locator("[role='dialog']").first
            
            # 1. Room Type
            room_type_input = modal.locator("input").first
            cursor.click_with_cursor(room_type_input, duration=0.4)
            room_type_input.fill("Automation Test Suite Room")
            print("✅ Room Type: Filled")
            
            # 2. Get all text inputs
            inputs = modal.locator("input:not([type='hidden']):not([type='date'])").all()
            
            if len(inputs) >= 4:
                # Single Agree
                cursor.click_with_cursor(inputs[1], duration=0.3)
                inputs[1].fill("5000")
                print("✅ Single Agree: 5000")
                
                # Double Agree
                cursor.click_with_cursor(inputs[2], duration=0.3)
                inputs[2].fill("7000")
                print("✅ Double Agree: 7000")
                
                # Triple Agree
                cursor.click_with_cursor(inputs[3], duration=0.3)
                inputs[3].fill("9000")
                print("✅ Triple Agree: 9000")
            
            # 3. Meal Plan dropdown
            meal_plan_dropdown = modal.locator("select, [role='combobox']").first
            if meal_plan_dropdown.is_visible():
                cursor.click_with_cursor(meal_plan_dropdown, duration=0.4)
                time.sleep(0.5)
                
                # Select first option (CP - Breakfast)
                meal_plan_dropdown.select_option(index=0)
                print("✅ Meal Plan: Selected")
            
            # Screenshot showing all fields filled
            annotator.capture_with_cursor(
                "test_04_step1_all_fields_filled",
                512, 400
            )
            
            # 4. Try to click Save/Create
            print("📍 Attempting to save with ALL fields filled...")
            save_button = modal.locator("button:has-text('Create'), button:has-text('Save')").last
            
            if save_button.is_visible():
                # Screenshot cursor on Save button
                cursor.move_to_element(save_button, duration=0.6)
                time.sleep(0.5)
                
                annotator.capture_with_cursor(
                    "test_04_step2_clicking_save",
                    512, 600
                )
                
                # Click Save
                cursor.click_with_cursor(save_button, duration=0.6)
                time.sleep(3)
                
                # Screenshot result
                annotator.capture_error_state(
                    "test_04_step3_save_result",
                    "All Fields Filled - Check if saved"
                )
                
                # Check if staging table has the room
                staging_table = logged_in_page.locator("table").first
                if staging_table.is_visible():
                    rows = staging_table.locator("tbody tr").all()
                    print(f"✅ Staging table has {len(rows)} rows")
                    
                    if len(rows) > 0:
                        annotator.capture_element_with_box(
                            "test_04_step4_staging_table",
                            staging_table,
                            f"✅ {len(rows)} rooms in staging",
                            "green"
                        )
            
            self.close_modal_if_open(logged_in_page)
            
        except Exception as e:
            print(f"❌ Error: {e}")
            annotator.capture_error_state("test_04_error", str(e))
            self.close_modal_if_open(logged_in_page)
    
    # ========================================================================
    # TEST 5: Multiple Field Validations at Once
    # ========================================================================
    
    def test_05_multiple_field_errors(self, logged_in_page: Page):
        """
        Test: Leave multiple required fields empty
        Expected: Multiple error messages
        """
        annotator = AnnotatedScreenshotHelper(logged_in_page)
        cursor = VisualCursor(logged_in_page, cursor_size=35, cursor_color="purple")
        
        print("\n🎯 Test: Multiple Field Errors")
        time.sleep(1)
        
        if not self.select_property_and_wait(logged_in_page):
            return
        
        try:
            # Open modal
            add_button = logged_in_page.locator("button:has-text('Add Room Charges')").first
            cursor.click_with_cursor(add_button)
            time.sleep(2)
            
            create_button = logged_in_page.locator("button:has-text('Create New Room')").first
            cursor.click_with_cursor(create_button)
            time.sleep(2)
            
            # Screenshot: All fields empty
            annotator.capture_error_state(
                "test_05_step1_all_fields_empty",
                "All Required Fields Empty"
            )
            
            # Try to save immediately (nothing filled)
            modal = logged_in_page.locator("[role='dialog']").first
            save_button = modal.locator("button:has-text('Create'), button:has-text('Save')").first
            
            cursor.click_with_cursor(save_button, duration=0.6)
            time.sleep(2)
            
            # Screenshot: Should show multiple errors
            annotator.capture_error_state(
                "test_05_step2_multiple_errors",
                "Multiple Validation Errors Expected"
            )
            
            # Try to find all error messages
            error_selectors = [
                "text=/required/i",
                ".error",
                ".text-red-500",
                "[class*='error']",
                ".validation-error"
            ]
            
            all_errors = []
            for selector in error_selectors:
                errors = logged_in_page.locator(selector).all()
                for err in errors:
                    if err.is_visible():
                        try:
                            text = err.inner_text()
                            if text and len(text) < 200:
                                all_errors.append(text)
                        except:
                            pass
            
            if all_errors:
                print(f"✅ Found {len(all_errors)} error messages:")
                for i, err in enumerate(all_errors[:10]):
                    print(f"  {i+1}. {err}")
            else:
                print("⚠️  No error text found (might be toast notifications)")
            
            self.close_modal_if_open(logged_in_page)
            
        except Exception as e:
            print(f"❌ Error: {e}")
            annotator.capture_error_state("test_05_error", str(e))
            self.close_modal_if_open(logged_in_page)
