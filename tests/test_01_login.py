import pytest
from playwright.sync_api import Page, expect
import time
from datetime import datetime
import os

class TestTariffManagementLogin:
    """Test class for Tariff Management Login functionality"""
        
    def test_login_page_loads(self, page: Page):
        """Test Case 1: Verify login page loads successfully"""
        page.set_viewport_size({"width": 1920, "height": 1080})
        page.goto("https://test-warsoft-v4.hummingbirdindia.com/property/tariff")
        time.sleep(2)
        expect(page).to_have_title("HummingBird - ERP - Warsoft ?v=4.0.29")
        expect(page.locator("text=Welcome back!")).to_be_visible()
        
        # Take screenshot
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        page.screenshot(path=f"assets/screenshots/01_login_page_{timestamp}.png")
        
    def test_login_with_valid_credentials(self, logged_in_page: Page):
        """Test Case 2: Verify user is logged in (using shared session)"""
        # Just verify we're logged in by checking we're not on login page
        logged_in_page.goto("https://test-warsoft-v4.hummingbirdindia.com/property/tariff")
        time.sleep(2)
        
        # Take screenshot after login
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        logged_in_page.screenshot(path=f"assets/screenshots/02_after_login_{timestamp}.png")
        
        # Verify successful login by checking if we're redirected
        expect(logged_in_page).not_to_have_url("**/login")
