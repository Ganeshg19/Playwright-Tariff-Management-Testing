import pytest
from playwright.sync_api import Page, expect
import time
from datetime import datetime
import os

class TestTariffManagement:
    """Test class for Tariff Management functionality with bug validation - Uses shared login session"""
    
    def test_01_navigate_to_tariff_page(self, logged_in_page: Page):
        """Test Case 3: Navigate to Tariff Management page (ONCE)"""
        logged_in_page.goto("https://test-warsoft-v4.hummingbirdindia.com/property/tariff")
        time.sleep(2)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        logged_in_page.screenshot(path=f"assets/screenshots/04_tariff_page_{timestamp}.png")
        
    def test_02_select_property(self, logged_in_page: Page):
        """Test Case 4: Select property from dropdown (NO REFRESH)"""
        # No page refresh - continue on same page
        time.sleep(1)
        
        # Click property dropdown
        logged_in_page.click("text=Property Name")
        time.sleep(1)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        logged_in_page.screenshot(path=f"assets/screenshots/05_property_dropdown_{timestamp}.png")
        
    def test_03_bug_checkbox_not_visible(self, logged_in_page: Page):
        """BUG #1: TAC Exceptions Checkbox not clearly visible (NO REFRESH)"""
        # No page refresh - continue on same page
        time.sleep(1)
        
        # Navigate to TAC Exceptions tab
        try:
            logged_in_page.click("text=TAC Exceptions", timeout=5000)
            time.sleep(1)
        except:
            pass
        
        # Take screenshot showing checkbox visibility issue
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        logged_in_page.screenshot(path=f"assets/bugs/bug_01_checkbox_not_visible_{timestamp}.png")
        
    def test_04_bug_filter_initial_space(self, logged_in_page: Page):
        """BUG #2: Control initial space in filter (NO REFRESH)"""
        # No page refresh - continue on same page
        time.sleep(1)
        
        # Try to type space in filter
        try:
            filter_input = logged_in_page.locator("input[placeholder*='Filter']").first
            filter_input.click()
            filter_input.fill(" test")
            time.sleep(1)
        except:
            pass
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        logged_in_page.screenshot(path=f"assets/bugs/bug_02_filter_initial_space_{timestamp}.png")
        
    def test_05_table_header_case(self, logged_in_page: Page):
        """BUG #3: Table header name is in caps (NO REFRESH)"""
        # No page refresh - continue on same page
        time.sleep(1)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        logged_in_page.screenshot(path=f"assets/bugs/bug_03_table_header_caps_{timestamp}.png")
