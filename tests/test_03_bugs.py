import pytest
from playwright.sync_api import Page
import time
from datetime import datetime

class TestTariffManagementBugs:
    """Test class specifically for bug validation (NO PAGE REFRESHES)"""
    
    def test_06_bug_table_heading_mismatch(self, logged_in_page: Page):
        """BUG #4: Table heading name difference (NO REFRESH)"""
        # No page refresh - continue on same page
        time.sleep(1)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        logged_in_page.screenshot(path=f"assets/bugs/bug_04_table_heading_mismatch_{timestamp}.png")
        
    def test_07_bug_tooltip_not_shown(self, logged_in_page: Page):
        """BUG #5: Tool tip data not showing (NO REFRESH)"""
        # No page refresh - continue on same page
        time.sleep(1)
        # Hover over tax inclusive field
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        logged_in_page.screenshot(path=f"assets/bugs/bug_05_tooltip_missing_{timestamp}.png")
        
    def test_08_bug_design_issue_background(self, logged_in_page: Page):
        """BUG #6: Design issue at background (NO REFRESH)"""
        # No page refresh - continue on same page
        time.sleep(1)
        # Click Add room charges button
        try:
            logged_in_page.click("text=Add room charges", timeout=5000)
            time.sleep(2)
        except:
            pass
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        logged_in_page.screenshot(path=f"assets/bugs/bug_06_design_background_{timestamp}.png")
        
    def test_09_bug_error_message_content(self, logged_in_page: Page):
        """BUG #7: Error message content unclear (NO REFRESH)"""
        # No page refresh - continue on same page
        time.sleep(1)
        # Click create without filling required fields
        try:
            logged_in_page.click("button:has-text('Create')", timeout=5000)
            time.sleep(1)
        except:
            pass
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        logged_in_page.screenshot(path=f"assets/bugs/bug_07_error_message_{timestamp}.png")
        
    def test_10_bug_date_picker_alignment(self, logged_in_page: Page):
        """BUG #8: Date picker icon alignment (NO REFRESH)"""
        # No page refresh - continue on same page
        time.sleep(1)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        logged_in_page.screenshot(path=f"assets/bugs/bug_08_date_picker_alignment_{timestamp}.png")
        
    def test_11_bug_room_image_not_fit(self, logged_in_page: Page):
        """BUG #9: Room image upload size not fit to the box (NO REFRESH)"""
        # No page refresh - continue on same page
        time.sleep(1)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        logged_in_page.screenshot(path=f"assets/bugs/bug_09_room_image_fit_{timestamp}.png")
