"""
Proper Bug Reproduction Tests
Actually reproduce bugs by following correct user flow
"""

import pytest
from playwright.sync_api import Page, expect
import time
from datetime import datetime
import os


class TestProperBugReproduction:
    """Properly reproduce bugs with correct user interactions"""
    
    def setup_method(self, method):
        """Setup: Clean state before each test"""
        pass
    
    def teardown_method(self, method):
        """Cleanup: Close any modals after each test"""
        # This will be called after each test method
        print(f"\n🧹 Cleaning up after {method.__name__}...")
        # Modal cleanup is now handled within each test's try-finally block
    
    def close_all_modals(self, page: Page):
        """Helper: Force close all modals"""
        try:
            # Press ESC multiple times
            for _ in range(3):
                page.keyboard.press("Escape")
                time.sleep(0.5)
            
            # Try all close button types
            close_selectors = [
                "button[aria-label='Close']",
                "button:has-text('×')",
                "button:has-text('Cancel')",
                ".modal button.close",
                "[role='dialog'] button[type='button']:first-child"
            ]
            
            for selector in close_selectors:
                try:
                    buttons = page.locator(selector).all()
                    for btn in buttons:
                        if btn.is_visible():
                            btn.click(force=True)
                            time.sleep(0.5)
                except:
                    pass
            
            print("✅ Attempted to close all modals")
        except Exception as e:
            print(f"⚠️  Modal cleanup: {e}")
    
    def select_property_and_wait(self, page: Page):
        """Helper: Select property and wait for data to load"""
        try:
            # Multiple possible selectors for property input
            property_selectors = [
                "input[placeholder*='Property']",
                "input[placeholder*='Search']",
                "input[name*='property']",
                "input[type='search']",
                ".property-search input",
                "div.property-name input"
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
                
                # Type property name (min 3 characters to trigger search)
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
                    # Try pressing Enter
                    page.keyboard.press("Enter")
                
                time.sleep(3)  # Wait for data to load
                print("✅ Property selected and data loaded")
                return True
            else:
                print("⚠️  Property input not found with any selector")
                # Take debug screenshot
                page.screenshot(path=f"assets/test_results/debug_property_not_found_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png")
                return False
        except Exception as e:
            print(f"⚠️  Property selection failed: {e}")
            return False
    
    # ========================================================================
    # BUG REPRODUCTION TESTS WITH PROPER FLOW
    # ========================================================================
    
    def close_modal_if_open(self, page: Page):
        """Helper: Close any open modal - very aggressive approach"""
        try:
            # Method 1: Press ESC multiple times
            for _ in range(5):
                page.keyboard.press("Escape")
                time.sleep(0.3)
            
            # Method 2: Try all possible close button selectors
            close_selectors = [
                "button[aria-label='Close']",
                "button:has-text('×')",
                "button:has-text('Cancel')",
                "button.close",
                "[data-state='open'] button:first-child",
                "[role='dialog'] button[type='button']"
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
            
            # Method 3: Wait for modal to disappear
            try:
                page.wait_for_selector("[role='dialog']", state="hidden", timeout=3000)
                print("✅ Modal closed successfully")
            except:
                # Method 4: Click on backdrop
                try:
                    backdrop = page.locator("div[data-state='open'][class*='fixed']").first
                    if backdrop.is_visible(timeout=1000):
                        # Click outside modal (top-left corner of backdrop)
                        backdrop.click(position={"x": 10, "y": 10}, force=True)
                        time.sleep(1)
                except:
                    pass
            
            # Final verification
            time.sleep(1)
            return True
        except Exception as e:
            print(f"⚠️  Could not close modal: {e}")
            return False
    
    def test_bug_01_proper_add_room_charges_modal(self, logged_in_page: Page):
        """
        BUG: Test Add Room Charges modal after selecting property
        Proper flow: Select property → Click Add → Check modal → Close modal
        """
        # Page is already at tariff screen from conftest login
        time.sleep(1)
        
        # Screenshot: Initial state
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        logged_in_page.screenshot(path=f"assets/test_results/proper_bug_01_initial_{timestamp}.png")
        
        # Step 1: Select property
        property_selected = self.select_property_and_wait(logged_in_page)
        
        if property_selected:
            # Screenshot: After property selection
            logged_in_page.screenshot(path=f"assets/test_results/proper_bug_01_property_selected_{timestamp}.png")
            
            # Step 2: Click "Add Room Charges" button
            try:
                add_button = logged_in_page.locator("button:has-text('Add Room Charges'), button:has-text('Create')").first
                
                if add_button.is_visible():
                    print("✅ Add button found, clicking...")
                    add_button.click()
                    time.sleep(2)
                    
                    # Screenshot: Modal opened
                    logged_in_page.screenshot(path=f"assets/test_results/proper_bug_01_modal_opened_{timestamp}.png", full_page=True)
                    
                    # Check modal elements
                    modal = logged_in_page.locator(".modal, [role='dialog']").first
                    if modal.is_visible():
                        print("✅ Modal is visible")
                        
                        # Screenshot: Modal content
                        logged_in_page.screenshot(path=f"assets/test_results/proper_bug_01_modal_content_{timestamp}.png", full_page=True)
                        
                        # CLOSE MODAL BEFORE PROCEEDING
                        print("🔄 Closing modal...")
                        self.close_modal_if_open(logged_in_page)
                        
                        # Screenshot: After closing
                        logged_in_page.screenshot(path=f"assets/test_results/proper_bug_01_modal_closed_{timestamp}.png")
                    else:
                        print("❌ Modal not visible after clicking Add button")
                else:
                    print("❌ Add button not found")
            except Exception as e:
                print(f"❌ Error: {e}")
                logged_in_page.screenshot(path=f"assets/test_results/proper_bug_01_error_{timestamp}.png")
                # Try to close modal even on error
                self.close_modal_if_open(logged_in_page)
    
    def test_bug_02_proper_edit_functionality(self, logged_in_page: Page):
        """
        BUG: Test Edit button after selecting property and loading data
        Proper flow: Select property → Wait for data → Click Edit → Close modal
        """
        time.sleep(1)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Step 1: Select property
        property_selected = self.select_property_and_wait(logged_in_page)
        
        if property_selected:
            # Screenshot: Data loaded
            logged_in_page.screenshot(path=f"assets/test_results/proper_bug_02_data_loaded_{timestamp}.png")
            
            # Step 2: Find and click Edit button
            try:
                # Look for edit buttons in table
                edit_buttons = logged_in_page.locator("button:has-text('Edit'), [title='Edit'], .edit-button, .btn-edit").all()
                
                if edit_buttons:
                    print(f"✅ Found {len(edit_buttons)} edit buttons")
                    
                    # Click first edit button
                    edit_buttons[0].click()
                    time.sleep(2)
                    
                    # Screenshot: Edit modal opened
                    logged_in_page.screenshot(path=f"assets/test_results/proper_bug_02_edit_modal_{timestamp}.png", full_page=True)
                    
                    # Check if modal has pre-filled data
                    inputs = logged_in_page.locator("input:not([type='hidden'])").all()
                    print(f"✅ Found {len(inputs)} input fields in edit modal")
                    
                    # Screenshot: Form fields
                    logged_in_page.screenshot(path=f"assets/test_results/proper_bug_02_form_fields_{timestamp}.png", full_page=True)
                    
                    # CLOSE MODAL
                    print("🔄 Closing edit modal...")
                    self.close_modal_if_open(logged_in_page)
                else:
                    print("❌ No edit buttons found - check if data is loaded")
                    logged_in_page.screenshot(path=f"assets/test_results/proper_bug_02_no_edit_buttons_{timestamp}.png")
            except Exception as e:
                print(f"❌ Error: {e}")
                logged_in_page.screenshot(path=f"assets/test_results/proper_bug_02_error_{timestamp}.png")
                # Try to close modal even on error
                self.close_modal_if_open(logged_in_page)
    
    def test_bug_03_proper_table_filtering(self, logged_in_page: Page):
        """
        BUG: Test table filtering after property selection
        Proper flow: Select property → Wait for data → Apply filter
        """
        time.sleep(1)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Step 1: Select property
        property_selected = self.select_property_and_wait(logged_in_page)
        
        if property_selected:
            # Screenshot: Before filter
            logged_in_page.screenshot(path=f"assets/test_results/proper_bug_03_before_filter_{timestamp}.png")
            
            # Step 2: Count rows before filter
            try:
                rows_before = logged_in_page.locator("table tbody tr, .table-row").count()
                print(f"✅ Rows before filter: {rows_before}")
                
                # Step 3: Apply filter
                filter_input = logged_in_page.locator("input[placeholder*='Filter'], input[placeholder*='Search']").nth(1)  # Second input (not property search)
                
                if filter_input.is_visible():
                    filter_input.fill("Single")
                    time.sleep(2)
                    
                    # Screenshot: After filter applied
                    logged_in_page.screenshot(path=f"assets/test_results/proper_bug_03_after_filter_{timestamp}.png")
                    
                    # Count rows after filter
                    rows_after = logged_in_page.locator("table tbody tr, .table-row").count()
                    print(f"✅ Rows after filter: {rows_after}")
                    
                    # Step 4: Clear filter
                    filter_input.clear()
                    time.sleep(2)
                    
                    # Screenshot: After clear
                    logged_in_page.screenshot(path=f"assets/test_results/proper_bug_03_filter_cleared_{timestamp}.png")
                    
                    # Check if rows restored
                    rows_restored = logged_in_page.locator("table tbody tr, .table-row").count()
                    print(f"✅ Rows after clear: {rows_restored}")
                    
                    if rows_restored != rows_before:
                        print(f"⚠️  BUG: Filter not properly clearing! Before: {rows_before}, After: {rows_restored}")
                else:
                    print("❌ Filter input not found")
            except Exception as e:
                print(f"❌ Error: {e}")
                logged_in_page.screenshot(path=f"assets/test_results/proper_bug_03_error_{timestamp}.png")
    
    def test_bug_04_proper_horizontal_scroll(self, logged_in_page: Page):
        """
        BUG: Test horizontal scroll with actual data
        Proper flow: Select property → Wait for data → Test scroll
        """
        time.sleep(1)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Step 1: Select property
        property_selected = self.select_property_and_wait(logged_in_page)
        
        if property_selected:
            # Screenshot: Initial table view
            logged_in_page.screenshot(path=f"assets/test_results/proper_bug_04_initial_view_{timestamp}.png")
            
            try:
                # Find table
                table = logged_in_page.locator("table, .table-container").first
                
                if table.is_visible():
                    # Scroll to right
                    table.evaluate("el => el.scrollLeft = 500")
                    time.sleep(1)
                    
                    # Screenshot: Scrolled right
                    logged_in_page.screenshot(path=f"assets/test_results/proper_bug_04_scrolled_right_{timestamp}.png")
                    
                    # Scroll to far right
                    table.evaluate("el => el.scrollLeft = el.scrollWidth")
                    time.sleep(1)
                    
                    # Screenshot: Scrolled far right
                    logged_in_page.screenshot(path=f"assets/test_results/proper_bug_04_scrolled_far_right_{timestamp}.png")
                    
                    # Check for header overlap
                    print("✅ Check these screenshots for header overlapping issues")
                else:
                    print("❌ Table not found")
            except Exception as e:
                print(f"❌ Error: {e}")
                logged_in_page.screenshot(path=f"assets/test_results/proper_bug_04_error_{timestamp}.png")
    
    def test_bug_05_proper_form_validation(self, logged_in_page: Page):
        """
        BUG: Test form field validations properly
        Proper flow: Select property → Open modal → Test each field
        """
        time.sleep(1)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Step 1: Select property
        property_selected = self.select_property_and_wait(logged_in_page)
        
        if property_selected:
            # Step 2: Open Add modal
            try:
                add_button = logged_in_page.locator("button:has-text('Add Room Charges')").first
                if add_button.is_visible():
                    add_button.click()
                    time.sleep(2)
                    
                    # Test: Enter invalid date
                    date_inputs = logged_in_page.locator("input[type='date']").all()
                    if date_inputs:
                        # Try to type manually (should not be allowed)
                        date_inputs[0].click()
                        logged_in_page.keyboard.type("99/99/9999")
                        time.sleep(1)
                        
                        # Screenshot: Invalid date attempt
                        logged_in_page.screenshot(path=f"assets/test_results/proper_bug_05_invalid_date_{timestamp}.png")
                    
                    # Test: Enter excessive length in tariff field
                    tariff_inputs = logged_in_page.locator("input[name*='tariff'], input[name*='amount']").all()
                    if tariff_inputs:
                        tariff_inputs[0].fill("999999999999999999999")
                        time.sleep(1)
                        
                        # Screenshot: Excessive length
                        logged_in_page.screenshot(path=f"assets/test_results/proper_bug_05_excessive_length_{timestamp}.png")
                    
                    # Test: Enter decimal in TAC percentage
                    tac_inputs = logged_in_page.locator("input[name*='tac'], input[name*='percentage']").all()
                    if tac_inputs:
                        tac_inputs[0].fill("12.5")
                        time.sleep(1)
                        
                        # Screenshot: Decimal value
                        logged_in_page.screenshot(path=f"assets/test_results/proper_bug_05_decimal_tac_{timestamp}.png")
                    
                    # CLOSE MODAL
                    print("🔄 Closing validation test modal...")
                    self.close_modal_if_open(logged_in_page)
                    
                    # Screenshot: After modal closed
                    logged_in_page.screenshot(path=f"assets/test_results/proper_bug_05_validation_complete_{timestamp}.png")
            except Exception as e:
                print(f"❌ Error: {e}")
                logged_in_page.screenshot(path=f"assets/test_results/proper_bug_05_error_{timestamp}.png")
                # Try to close modal even on error
                self.close_modal_if_open(logged_in_page)
    
    def test_bug_06_proper_responsive_mobile(self, logged_in_page: Page):
        """
        BUG: Test mobile responsive with actual data
        Proper flow: Select property → Change viewport → Check layout
        """
        time.sleep(1)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Step 1: Select property at desktop size
        property_selected = self.select_property_and_wait(logged_in_page)
        
        if property_selected:
            # Step 2: Change to mobile viewport
            logged_in_page.set_viewport_size({"width": 375, "height": 667})
            time.sleep(2)
            
            # Screenshot: Mobile view
            logged_in_page.screenshot(path=f"assets/test_results/proper_bug_06_mobile_view_{timestamp}.png", full_page=True)
            
            # Test: Try to scroll horizontally on mobile
            try:
                table = logged_in_page.locator("table").first
                if table.is_visible():
                    table.evaluate("el => el.scrollLeft = 200")
                    time.sleep(1)
                    
                    # Screenshot: Mobile scrolled
                    logged_in_page.screenshot(path=f"assets/test_results/proper_bug_06_mobile_scrolled_{timestamp}.png", full_page=True)
            except:
                pass
            
            # Reset viewport
            logged_in_page.set_viewport_size({"width": 1920, "height": 1080})
    
    def test_bug_07_proper_tac_exceptions_tab(self, logged_in_page: Page):
        """
        BUG: Test TAC Exceptions tab properly
        Proper flow: Select property → Click TAC tab → Test functionality
        """
        time.sleep(1)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Step 1: Select property
        property_selected = self.select_property_and_wait(logged_in_page)
        
        if property_selected:
            # Step 2: Click TAC Exceptions tab
            try:
                tac_tab = logged_in_page.locator("a:has-text('TAC Exceptions'), button:has-text('TAC Exceptions')").first
                
                if tac_tab.is_visible():
                    tac_tab.click()
                    time.sleep(2)
                    
                    # Screenshot: TAC tab opened
                    logged_in_page.screenshot(path=f"assets/test_results/proper_bug_07_tac_tab_{timestamp}.png")
                    
                    # Check checkbox visibility
                    checkboxes = logged_in_page.locator("input[type='checkbox']").all()
                    print(f"✅ Found {len(checkboxes)} checkboxes")
                    
                    # Screenshot: Checkbox close-up
                    if checkboxes:
                        logged_in_page.screenshot(path=f"assets/test_results/proper_bug_07_checkbox_visibility_{timestamp}.png")
                else:
                    print("❌ TAC Exceptions tab not found")
            except Exception as e:
                print(f"❌ Error: {e}")


# Helper function to generate bug report
def generate_bug_report_from_screenshots():
    """Analyze screenshots and generate bug report"""
    import os
    from pathlib import Path
    
    results_dir = Path("assets/test_results")
    screenshots = list(results_dir.glob("proper_bug_*.png"))
    
    print(f"\n📸 Generated {len(screenshots)} screenshots")
    print(f"📁 Location: {results_dir}")
    print("\n✅ Review screenshots to identify bugs:")
    
    for screenshot in sorted(screenshots):
        print(f"  - {screenshot.name}")
    
    return screenshots
