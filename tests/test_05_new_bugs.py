import pytest
from playwright.sync_api import Page, expect
import time
from datetime import datetime

class TestTariffManagementAdditionalBugs:
    """Additional bug validation tests based on screen analysis - Deep testing"""
    
    def test_23_property_name_required_validation(self, logged_in_page: Page):
        """NEW BUG #21: Property Name required validation message position (NO REFRESH)"""
        # No page refresh - continue on same page
        time.sleep(1)
        
        # Try to add room charges without selecting property
        try:
            logged_in_page.click("button:has-text('Add Room Charges')", timeout=5000)
            time.sleep(1)
        except:
            pass
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        logged_in_page.screenshot(path=f"assets/bugs/bug_21_property_required_validation_{timestamp}.png")
        
    def test_24_no_records_found_message_styling(self, logged_in_page: Page):
        """NEW BUG #22: 'No records found' message styling and alignment"""
        # No page refresh - continue on same page
        time.sleep(1)
        
        # Check the "No records found" message alignment and styling
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        logged_in_page.screenshot(path=f"assets/bugs/bug_22_no_records_styling_{timestamp}.png")
        
    def test_25_table_column_width_consistency(self, logged_in_page: Page):
        """NEW BUG #23: Table column widths not consistent"""
        # No page refresh - continue on same page
        time.sleep(1)
        
        # Select a property to load data
        try:
            property_input = logged_in_page.locator('input[placeholder*="Search Property"]').first
            property_input.click()
            property_input.fill("test")
            time.sleep(1)
        except:
            pass
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        logged_in_page.screenshot(path=f"assets/bugs/bug_23_column_width_{timestamp}.png")
        
    def test_26_history_button_visibility(self, logged_in_page: Page):
        """NEW BUG #24: History button icon visibility and size"""
        # No page refresh - continue on same page
        time.sleep(1)
        
        # Check History button
        try:
            logged_in_page.locator("button:has-text('History')").hover()
            time.sleep(1)
        except:
            pass
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        logged_in_page.screenshot(path=f"assets/bugs/bug_24_history_button_{timestamp}.png")
        
    def test_27_filter_search_icon_alignment(self, logged_in_page: Page):
        """NEW BUG #25: Filter search icon alignment in table"""
        # No page refresh - continue on same page
        time.sleep(1)
        
        # Check filter icon alignment
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        logged_in_page.screenshot(path=f"assets/bugs/bug_25_filter_icon_alignment_{timestamp}.png")
        
    def test_28_table_horizontal_scroll_indicator(self, logged_in_page: Page):
        """NEW BUG #26: Missing horizontal scroll indicator for table"""
        # No page refresh - continue on same page
        time.sleep(1)
        
        # Check if horizontal scroll is visible/indicated
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        logged_in_page.screenshot(path=f"assets/bugs/bug_26_scroll_indicator_{timestamp}.png")
        
    def test_29_button_hover_effects(self, logged_in_page: Page):
        """NEW BUG #27: Inconsistent button hover effects"""
        # No page refresh - continue on same page
        time.sleep(1)
        
        # Hover over Add Room Charges button
        try:
            logged_in_page.locator("button:has-text('Add Room Charges')").hover()
            time.sleep(1)
        except:
            pass
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        logged_in_page.screenshot(path=f"assets/bugs/bug_27_button_hover_{timestamp}.png")
        
    def test_30_tac_exceptions_tab_styling(self, logged_in_page: Page):
        """NEW BUG #28: TAC Exceptions tab styling inconsistency"""
        # No page refresh - continue on same page
        time.sleep(1)
        
        # Check TAC Exceptions tab styling
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        logged_in_page.screenshot(path=f"assets/bugs/bug_28_tac_tab_styling_{timestamp}.png")
        
    def test_31_search_property_placeholder_text(self, logged_in_page: Page):
        """NEW BUG #29: Search Property placeholder text clarity"""
        # No page refresh - continue on same page
        time.sleep(1)
        
        # Focus on property name input
        try:
            property_input = logged_in_page.locator('input[placeholder*="Search"]').first
            property_input.click()
            time.sleep(1)
        except:
            pass
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        logged_in_page.screenshot(path=f"assets/bugs/bug_29_placeholder_text_{timestamp}.png")
        
    def test_32_breadcrumb_navigation(self, logged_in_page: Page):
        """NEW BUG #30: Breadcrumb navigation clarity"""
        # No page refresh - continue on same page
        time.sleep(1)
        
        # Check breadcrumb navigation
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        logged_in_page.screenshot(path=f"assets/bugs/bug_30_breadcrumb_{timestamp}.png")
        
    def test_33_responsive_design_small_screen(self, logged_in_page: Page):
        """NEW BUG #31: Responsive design issues on smaller viewports"""
        # Change viewport to tablet size
        logged_in_page.set_viewport_size({"width": 768, "height": 1024})
        # No page refresh - continue on same page
        time.sleep(1)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        logged_in_page.screenshot(path=f"assets/bugs/bug_31_responsive_tablet_{timestamp}.png")
        
        # Reset viewport
        logged_in_page.set_viewport_size({"width": 1920, "height": 1080})
        
    def test_34_mobile_responsive_design(self, logged_in_page: Page):
        """NEW BUG #32: Mobile responsive design issues"""
        # Change viewport to mobile size
        logged_in_page.set_viewport_size({"width": 375, "height": 667})
        # No page refresh - continue on same page
        time.sleep(1)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        logged_in_page.screenshot(path=f"assets/bugs/bug_32_responsive_mobile_{timestamp}.png")
        
        # Reset viewport
        logged_in_page.set_viewport_size({"width": 1920, "height": 1080})
        
    def test_35_loading_indicator_missing(self, logged_in_page: Page):
        """NEW BUG #33: Missing loading indicator when fetching data"""
        # No page refresh - continue on same page
        
        # Try to trigger loading state
        try:
            property_input = logged_in_page.locator('input[placeholder*="Search"]').first
            property_input.click()
            property_input.fill("a")
            # Capture immediately to see if loader shows
            time.sleep(0.5)
        except:
            pass
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        logged_in_page.screenshot(path=f"assets/bugs/bug_33_loading_indicator_{timestamp}.png")
        
    def test_36_keyboard_navigation(self, logged_in_page: Page):
        """NEW BUG #34: Keyboard navigation accessibility"""
        # No page refresh - continue on same page
        time.sleep(1)
        
        # Try tab navigation
        logged_in_page.keyboard.press("Tab")
        time.sleep(0.5)
        logged_in_page.keyboard.press("Tab")
        time.sleep(0.5)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        logged_in_page.screenshot(path=f"assets/bugs/bug_34_keyboard_nav_{timestamp}.png")
        
    def test_37_focus_indicator_visibility(self, logged_in_page: Page):
        """NEW BUG #35: Focus indicator not clearly visible"""
        # No page refresh - continue on same page
        time.sleep(1)
        
        # Tab to elements to check focus
        for i in range(5):
            logged_in_page.keyboard.press("Tab")
            time.sleep(0.3)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        logged_in_page.screenshot(path=f"assets/bugs/bug_35_focus_indicator_{timestamp}.png")
        
    def test_38_error_message_color_contrast(self, logged_in_page: Page):
        """NEW BUG #36: Error message color contrast for accessibility"""
        # No page refresh - continue on same page
        time.sleep(1)
        
        # Trigger an error
        try:
            logged_in_page.click("button:has-text('Add Room Charges')", timeout=3000)
            time.sleep(1)
        except:
            pass
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        logged_in_page.screenshot(path=f"assets/bugs/bug_36_error_contrast_{timestamp}.png")
        
    def test_39_table_header_sticky(self, logged_in_page: Page):
        """NEW BUG #37: Table header not sticky on scroll"""
        # No page refresh - continue on same page
        time.sleep(1)
        
        # Try to scroll if data exists
        try:
            logged_in_page.mouse.wheel(0, 500)
            time.sleep(1)
        except:
            pass
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        logged_in_page.screenshot(path=f"assets/bugs/bug_37_sticky_header_{timestamp}.png")
        
    def test_40_empty_state_icon(self, logged_in_page: Page):
        """NEW BUG #38: Empty state missing icon/illustration"""
        # No page refresh - continue on same page
        time.sleep(1)
        
        # Check empty state when no property selected
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        logged_in_page.screenshot(path=f"assets/bugs/bug_38_empty_state_{timestamp}.png")
        
    def test_41_action_buttons_spacing(self, logged_in_page: Page):
        """NEW BUG #39: Inconsistent spacing between action buttons"""
        # No page refresh - continue on same page
        time.sleep(1)
        
        # Check button spacing
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        logged_in_page.screenshot(path=f"assets/bugs/bug_39_button_spacing_{timestamp}.png")
        
    def test_42_dropdown_animation_smoothness(self, logged_in_page: Page):
        """NEW BUG #40: Dropdown animation not smooth"""
        # No page refresh - continue on same page
        time.sleep(1)
        
        # Click on property dropdown
        try:
            property_input = logged_in_page.locator('input[placeholder*="Search"]').first
            property_input.click()
            time.sleep(0.5)  # Capture during animation
        except:
            pass
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        logged_in_page.screenshot(path=f"assets/bugs/bug_40_dropdown_animation_{timestamp}.png")
