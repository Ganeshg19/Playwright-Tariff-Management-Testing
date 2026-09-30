"""
Advanced Tariff Management Test Suite
Comprehensive testing with creative scenarios, user flows, and bug detection
"""

import pytest
from playwright.sync_api import Page, expect
import time
from datetime import datetime
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from tests.conftest_screenshot import AnnotatedScreenshot


class TestAdvancedTariffManagement:
    """Advanced test suite covering all user flows and edge cases"""
    
    # ============================================================================
    # PROPERTY SEARCH & SELECTION TESTS
    # ============================================================================
    
    def test_01_property_search_empty_state(self, logged_in_page: Page, annotated_screenshot):
        """BUG HUNT: Test property search with empty state"""
        logged_in_page.goto("https://test-warsoft-v4.hummingbirdindia.com/property/tariff")
        time.sleep(2)
        
        # Check initial state - no property selected
        # Should show appropriate message or disabled state
        annotated_screenshot.capture_bug('test_01_empty_state')
        
        # Try actions without property selection
        try:
            add_button = logged_in_page.locator("button:has-text('Add Room Charges')")
            if add_button.is_visible():
                add_button.click()
                time.sleep(1)
                # Should show validation error
                annotated_screenshot.capture_bug('test_01_no_property_validation')
        except:
            pass
    
    def test_02_property_search_partial_match(self, logged_in_page: Page, annotated_screenshot):
        """BUG HUNT: Test property search with partial text"""
        time.sleep(1)
        
        # Test partial search
        search_input = logged_in_page.locator("input[placeholder*='Search Property'], input[placeholder*='Property']").first
        
        if search_input.is_visible():
            # Test with partial text
            search_input.fill("AM")
            time.sleep(1)
            annotated_screenshot.capture_bug('test_02_partial_search')
            
            # Check dropdown appears
            dropdown = logged_in_page.locator(".dropdown-menu, [role='listbox']")
            time.sleep(0.5)
            
            # Test special characters
            search_input.fill("@#$%")
            time.sleep(1)
            annotated_screenshot.capture_bug('test_02_special_chars_search')
    
    def test_03_property_dropdown_keyboard_navigation(self, logged_in_page: Page, annotated_screenshot):
        """BUG HUNT: Test keyboard navigation in property dropdown"""
        time.sleep(1)
        
        search_input = logged_in_page.locator("input[placeholder*='Search Property'], input[placeholder*='Property']").first
        
        if search_input.is_visible():
            search_input.click()
            time.sleep(0.5)
            
            # Test arrow key navigation
            logged_in_page.keyboard.press("ArrowDown")
            time.sleep(0.5)
            annotated_screenshot.capture_bug('test_03_arrow_down')
            
            logged_in_page.keyboard.press("ArrowUp")
            time.sleep(0.5)
            
            # Test Enter key
            logged_in_page.keyboard.press("Enter")
            time.sleep(1)
            annotated_screenshot.capture_bug('test_03_enter_selection')
    
    # ============================================================================
    # TABLE & DATA DISPLAY TESTS
    # ============================================================================
    
    def test_04_table_horizontal_scroll(self, logged_in_page: Page, annotated_screenshot):
        """BUG HUNT: Test horizontal scrolling behavior"""
        time.sleep(1)
        
        # Capture table at default position
        annotated_screenshot.capture_bug('test_04_scroll_start')
        
        # Scroll horizontally if table exists
        try:
            table = logged_in_page.locator("table, .table-container").first
            
            # Scroll to right
            table.evaluate("el => el.scrollLeft = el.scrollWidth")
            time.sleep(1)
            annotated_screenshot.capture_bug('test_04_scroll_end')
            
            # Scroll to middle
            table.evaluate("el => el.scrollLeft = el.scrollWidth / 2")
            time.sleep(1)
            annotated_screenshot.capture_bug('test_04_scroll_middle')
            
            # Check if headers stick/overlap
            annotated_screenshot.capture_bug('test_04_header_overlap_check')
        except:
            pass
    
    def test_05_table_column_sorting(self, logged_in_page: Page, annotated_screenshot):
        """BUG HUNT: Test column sorting functionality"""
        time.sleep(1)
        
        try:
            # Click each column header to test sorting
            headers = logged_in_page.locator("th, .table-header").all()
            
            for i, header in enumerate(headers[:3]):  # Test first 3 columns
                header.click()
                time.sleep(1)
                annotated_screenshot.capture_bug(f'test_05_sort_column_{i}_asc')
                
                # Click again for descending
                header.click()
                time.sleep(1)
                annotated_screenshot.capture_bug(f'test_05_sort_column_{i}_desc')
        except:
            pass
    
    def test_06_table_data_filtering(self, logged_in_page: Page, annotated_screenshot):
        """BUG HUNT: Test table filtering after property selection"""
        time.sleep(1)
        
        # Find filter input
        filter_inputs = logged_in_page.locator("input[placeholder*='Filter'], input[placeholder*='Search']").all()
        
        for i, filter_input in enumerate(filter_inputs):
            if filter_input.is_visible():
                # Test normal filtering
                filter_input.fill("test")
                time.sleep(1)
                annotated_screenshot.capture_bug(f'test_06_filter_{i}_normal')
                
                # Test with numbers
                filter_input.clear()
                filter_input.fill("123")
                time.sleep(1)
                annotated_screenshot.capture_bug(f'test_06_filter_{i}_numbers')
                
                # Test with special chars
                filter_input.clear()
                filter_input.fill("@#$")
                time.sleep(1)
                annotated_screenshot.capture_bug(f'test_06_filter_{i}_special')
                
                # Clear filter
                filter_input.clear()
                time.sleep(1)
    
    def test_07_table_pagination_edge_cases(self, logged_in_page: Page, annotated_screenshot):
        """BUG HUNT: Test pagination edge cases"""
        time.sleep(1)
        
        try:
            # Check if pagination exists
            pagination = logged_in_page.locator(".pagination, [aria-label='pagination']")
            
            if pagination.is_visible():
                # Test first page
                annotated_screenshot.capture_bug('test_07_pagination_first')
                
                # Test last page button
                last_button = logged_in_page.locator("button:has-text('Last'), .pagination-last")
                if last_button.is_visible():
                    last_button.click()
                    time.sleep(1)
                    annotated_screenshot.capture_bug('test_07_pagination_last')
                
                # Test invalid page number input
                page_input = logged_in_page.locator("input[type='number'].page-input")
                if page_input.is_visible():
                    page_input.fill("999")
                    time.sleep(1)
                    annotated_screenshot.capture_bug('test_07_pagination_invalid')
        except:
            pass
    
    # ============================================================================
    # RESPONSIVE DESIGN TESTS
    # ============================================================================
    
    def test_08_responsive_mobile_320px(self, logged_in_page: Page, annotated_screenshot):
        """BUG HUNT: Test mobile view (iPhone SE)"""
        # Set viewport to mobile size
        logged_in_page.set_viewport_size({"width": 320, "height": 568})
        time.sleep(1)
        
        annotated_screenshot.capture_bug('test_08_mobile_320px')
        
        # Test navigation menu
        try:
            menu_button = logged_in_page.locator("button.navbar-toggler, .menu-button")
            if menu_button.is_visible():
                menu_button.click()
                time.sleep(1)
                annotated_screenshot.capture_bug('test_08_mobile_menu_open')
        except:
            pass
    
    def test_09_responsive_tablet_768px(self, logged_in_page: Page, annotated_screenshot):
        """BUG HUNT: Test tablet view (iPad)"""
        logged_in_page.set_viewport_size({"width": 768, "height": 1024})
        time.sleep(1)
        
        annotated_screenshot.capture_bug('test_09_tablet_768px')
        
        # Test table responsiveness
        try:
            table = logged_in_page.locator("table").first
            if table.is_visible():
                # Check if table is scrollable
                annotated_screenshot.capture_bug('test_09_tablet_table')
        except:
            pass
    
    def test_10_responsive_desktop_1920px(self, logged_in_page: Page, annotated_screenshot):
        """BUG HUNT: Test large desktop view"""
        logged_in_page.set_viewport_size({"width": 1920, "height": 1080})
        time.sleep(1)
        
        annotated_screenshot.capture_bug('test_10_desktop_1920px')
    
    def test_11_responsive_ultra_wide_2560px(self, logged_in_page: Page, annotated_screenshot):
        """BUG HUNT: Test ultra-wide monitor"""
        logged_in_page.set_viewport_size({"width": 2560, "height": 1440})
        time.sleep(1)
        
        annotated_screenshot.capture_bug('test_11_ultra_wide_2560px')
        
        # Check for layout issues on wide screens
        # Reset viewport
        logged_in_page.set_viewport_size({"width": 1920, "height": 1080})
    
    # ============================================================================
    # MODAL & FORM SUBMISSION TESTS
    # ============================================================================
    
    def test_12_add_room_charges_modal_open(self, logged_in_page: Page, annotated_screenshot):
        """BUG HUNT: Test Add Room Charges modal opening"""
        time.sleep(1)
        
        try:
            add_button = logged_in_page.locator("button:has-text('Add Room Charges'), button:has-text('Create')")
            
            if add_button.is_visible():
                add_button.click()
                time.sleep(2)
                annotated_screenshot.capture_bug('test_12_modal_opened')
                
                # Check modal backdrop
                backdrop = logged_in_page.locator(".modal-backdrop, .overlay")
                if backdrop.is_visible():
                    annotated_screenshot.capture_bug('test_12_modal_backdrop')
        except Exception as e:
            print(f"Modal test error: {e}")
    
    def test_13_modal_form_validation_empty(self, logged_in_page: Page, annotated_screenshot):
        """BUG HUNT: Test form submission with empty fields"""
        time.sleep(1)
        
        try:
            # Try to submit without filling fields
            save_button = logged_in_page.locator("button:has-text('Save'), button:has-text('Submit')")
            
            if save_button.is_visible():
                save_button.click()
                time.sleep(1)
                annotated_screenshot.capture_bug('test_13_empty_form_validation')
                
                # Check for validation messages
                errors = logged_in_page.locator(".error-message, .invalid-feedback, .alert-danger").all()
                if errors:
                    annotated_screenshot.capture_bug('test_13_validation_errors')
        except:
            pass
    
    def test_14_modal_form_field_validation(self, logged_in_page: Page, annotated_screenshot):
        """BUG HUNT: Test individual field validations"""
        time.sleep(1)
        
        try:
            # Test date field
            date_inputs = logged_in_page.locator("input[type='date']").all()
            for i, date_input in enumerate(date_inputs[:2]):
                if date_input.is_visible():
                    # Try invalid date
                    date_input.fill("99/99/9999")
                    time.sleep(0.5)
                    annotated_screenshot.capture_bug(f'test_14_invalid_date_{i}')
            
            # Test number fields
            number_inputs = logged_in_page.locator("input[type='number']").all()
            for i, num_input in enumerate(number_inputs[:2]):
                if num_input.is_visible():
                    # Try negative number
                    num_input.fill("-999")
                    time.sleep(0.5)
                    annotated_screenshot.capture_bug(f'test_14_negative_number_{i}')
                    
                    # Try decimal where not allowed
                    num_input.fill("123.456")
                    time.sleep(0.5)
        except:
            pass
    
    def test_15_modal_close_methods(self, logged_in_page: Page, annotated_screenshot):
        """BUG HUNT: Test different ways to close modal"""
        time.sleep(1)
        
        try:
            # Test close button
            close_buttons = logged_in_page.locator("button.close, button:has-text('Cancel'), button:has-text('×')").all()
            
            for close_btn in close_buttons:
                if close_btn.is_visible():
                    close_btn.click()
                    time.sleep(1)
                    annotated_screenshot.capture_bug('test_15_modal_closed')
                    break
            
            # Test ESC key
            logged_in_page.keyboard.press("Escape")
            time.sleep(1)
            annotated_screenshot.capture_bug('test_15_esc_key')
            
            # Test clicking backdrop
            backdrop = logged_in_page.locator(".modal-backdrop")
            if backdrop.is_visible():
                backdrop.click()
                time.sleep(1)
        except:
            pass
    
    # ============================================================================
    # TAC EXCEPTIONS TAB TESTS
    # ============================================================================
    
    def test_16_tac_exceptions_tab_switch(self, logged_in_page: Page, annotated_screenshot):
        """BUG HUNT: Test TAC Exceptions tab functionality"""
        time.sleep(1)
        
        try:
            tac_tab = logged_in_page.locator("text=TAC Exceptions, a:has-text('TAC Exceptions')")
            
            if tac_tab.is_visible():
                tac_tab.click()
                time.sleep(2)
                annotated_screenshot.capture_bug('test_16_tac_tab_opened')
                
                # Test checkbox visibility
                checkboxes = logged_in_page.locator("input[type='checkbox']").all()
                annotated_screenshot.capture_bug('test_16_tac_checkboxes')
                
                # Test TAC percentage input
                tac_input = logged_in_page.locator("input[name*='tac'], input[name*='percentage']").first
                if tac_input.is_visible():
                    tac_input.fill("12.5")
                    time.sleep(1)
                    annotated_screenshot.capture_bug('test_16_tac_percentage_decimal')
        except:
            pass
    
    # ============================================================================
    # USER FLOW TESTS - COMPLETE WORKFLOWS
    # ============================================================================
    
    def test_17_complete_userflow_add_tariff(self, logged_in_page: Page, annotated_screenshot):
        """BUG HUNT: Complete user flow - Add new tariff"""
        time.sleep(1)
        
        # Step 1: Select property
        annotated_screenshot.capture_bug('test_17_step1_select_property')
        
        # Step 2: Click Add Room Charges
        try:
            add_btn = logged_in_page.locator("button:has-text('Add Room Charges')").first
            if add_btn.is_visible():
                add_btn.click()
                time.sleep(2)
                annotated_screenshot.capture_bug('test_17_step2_open_modal')
        except:
            pass
        
        # Step 3: Fill form fields
        annotated_screenshot.capture_bug('test_17_step3_form_state')
        
        # Step 4: Try to save
        try:
            save_btn = logged_in_page.locator("button:has-text('Save')").first
            if save_btn.is_visible():
                save_btn.click()
                time.sleep(2)
                annotated_screenshot.capture_bug('test_17_step4_save_attempt')
        except:
            pass
        
        # Step 5: Check result
        annotated_screenshot.capture_bug('test_17_step5_result')
    
    def test_18_complete_userflow_edit_tariff(self, logged_in_page: Page, annotated_screenshot):
        """BUG HUNT: Complete user flow - Edit existing tariff"""
        time.sleep(1)
        
        try:
            # Find edit button
            edit_btns = logged_in_page.locator("button:has-text('Edit'), .edit-icon, [title='Edit']").all()
            
            if edit_btns:
                edit_btns[0].click()
                time.sleep(2)
                annotated_screenshot.capture_bug('test_18_edit_modal_opened')
                
                # Modify field
                inputs = logged_in_page.locator("input:not([type='hidden'])").all()
                if inputs:
                    inputs[0].fill("Modified Value")
                    time.sleep(1)
                    annotated_screenshot.capture_bug('test_18_field_modified')
                
                # Save changes
                save_btn = logged_in_page.locator("button:has-text('Save'), button:has-text('Update')").first
                if save_btn.is_visible():
                    save_btn.click()
                    time.sleep(2)
                    annotated_screenshot.capture_bug('test_18_save_result')
        except:
            pass
    
    def test_19_complete_userflow_delete_tariff(self, logged_in_page: Page, annotated_screenshot):
        """BUG HUNT: Complete user flow - Delete tariff"""
        time.sleep(1)
        
        try:
            # Find delete button
            delete_btns = logged_in_page.locator("button:has-text('Delete'), .delete-icon, [title='Delete']").all()
            
            if delete_btns:
                delete_btns[0].click()
                time.sleep(1)
                annotated_screenshot.capture_bug('test_19_delete_confirmation')
                
                # Confirm deletion
                confirm_btn = logged_in_page.locator("button:has-text('Yes'), button:has-text('Confirm'), button:has-text('Delete')").first
                if confirm_btn.is_visible():
                    # Take screenshot before confirming (don't actually delete)
                    annotated_screenshot.capture_bug('test_19_before_delete')
        except:
            pass
    
    # ============================================================================
    # EDGE CASE & ERROR HANDLING TESTS
    # ============================================================================
    
    def test_20_concurrent_actions(self, logged_in_page: Page, annotated_screenshot):
        """BUG HUNT: Test rapid clicking and concurrent actions"""
        time.sleep(1)
        
        try:
            # Rapid click on same button
            button = logged_in_page.locator("button").first
            if button.is_visible():
                for i in range(5):
                    button.click()
                    time.sleep(0.1)
                
                time.sleep(1)
                annotated_screenshot.capture_bug('test_20_rapid_clicks')
        except:
            pass
    
    def test_21_session_timeout_behavior(self, logged_in_page: Page, annotated_screenshot):
        """BUG HUNT: Check behavior after extended inactivity"""
        time.sleep(1)
        
        # Capture current state
        annotated_screenshot.capture_bug('test_21_before_timeout')
        
        # Wait for a bit (simulating inactivity)
        time.sleep(3)
        
        # Try to perform action
        try:
            logged_in_page.reload()
            time.sleep(2)
            annotated_screenshot.capture_bug('test_21_after_reload')
        except:
            pass
    
    def test_22_browser_back_forward(self, logged_in_page: Page, annotated_screenshot):
        """BUG HUNT: Test browser back/forward buttons"""
        time.sleep(1)
        
        # Navigate away and back
        try:
            logged_in_page.go_back()
            time.sleep(2)
            annotated_screenshot.capture_bug('test_22_after_back')
            
            logged_in_page.go_forward()
            time.sleep(2)
            annotated_screenshot.capture_bug('test_22_after_forward')
        except:
            pass
    
    def test_23_network_interruption_simulation(self, logged_in_page: Page, annotated_screenshot):
        """BUG HUNT: Test behavior during network issues"""
        time.sleep(1)
        
        try:
            # Set offline mode
            context = logged_in_page.context
            context.set_offline(True)
            time.sleep(1)
            
            # Try to perform action
            logged_in_page.reload()
            time.sleep(2)
            annotated_screenshot.capture_bug('test_23_offline_mode')
            
            # Go back online
            context.set_offline(False)
            time.sleep(1)
        except:
            pass
    
    def test_24_copy_paste_functionality(self, logged_in_page: Page, annotated_screenshot):
        """BUG HUNT: Test copy-paste in various fields"""
        time.sleep(1)
        
        try:
            # Test in input fields
            inputs = logged_in_page.locator("input[type='text'], input[type='number']").all()
            
            for input_field in inputs[:2]:
                if input_field.is_visible():
                    # Type and copy
                    input_field.fill("Test Data 123")
                    logged_in_page.keyboard.press("Control+A")
                    logged_in_page.keyboard.press("Control+C")
                    time.sleep(0.5)
                    
                    # Paste
                    input_field.clear()
                    logged_in_page.keyboard.press("Control+V")
                    time.sleep(0.5)
                    annotated_screenshot.capture_bug('test_24_paste_result')
                    break
        except:
            pass
    
    def test_25_print_preview_functionality(self, logged_in_page: Page, annotated_screenshot):
        """BUG HUNT: Test print preview"""
        time.sleep(1)
        
        # Trigger print dialog
        try:
            logged_in_page.keyboard.press("Control+P")
            time.sleep(2)
            annotated_screenshot.capture_bug('test_25_print_preview')
            
            # Close print dialog
            logged_in_page.keyboard.press("Escape")
            time.sleep(1)
        except:
            pass


# Additional helper function for dynamic test generation
def generate_bug_report(test_results):
    """Generate comprehensive bug report from test results"""
    report = {
        'total_tests': len(test_results),
        'bugs_found': [],
        'screenshots': [],
        'severity': {
            'critical': 0,
            'high': 0,
            'medium': 0,
            'low': 0
        }
    }
    return report
