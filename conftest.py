import pytest
from playwright.sync_api import Page, Browser
import time
import os
import sys
from datetime import datetime

# Add utils to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'utils'))


class AnnotatedScreenshot:
    """Helper class for taking test screenshots"""
    
    def __init__(self, page: Page):
        self.page = page
        self.test_results_dir = "assets/test_results"
        os.makedirs(self.test_results_dir, exist_ok=True)
    
    def capture_bug(self, test_name: str):
        """Capture screenshot for testing"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{test_name}_{timestamp}.png"
        filepath = os.path.join(self.test_results_dir, filename)
        
        try:
            self.page.screenshot(path=filepath, full_page=True)
            print(f"📸 Screenshot: {filepath}")
        except Exception as e:
            print(f"⚠️  Screenshot failed: {e}")
        
        return filepath


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {
            "width": 1920,
            "height": 1080,
        },
    }

@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return {
        **browser_type_launch_args,
        "headless": False,
        "slow_mo": 1000,  # milliseconds
    }

@pytest.fixture(scope="session")
def logged_in_page(browser: Browser):
    """
    Session-scoped fixture that logs in once and reuses the same page for all tests.
    This significantly reduces test execution time.
    """
    context = browser.new_context(
        viewport={"width": 1920, "height": 1080}
    )
    page = context.new_page()
    
    # Perform login once
    page.goto("https://test-warsoft-v4.hummingbirdindia.com/property/tariff")
    time.sleep(2)
    
    # Fill email
    email_input = page.locator('input[placeholder="guest@hummingbirdindia.com"]')
    email_input.click()
    page.keyboard.press("Control+A")
    email_input.fill("anu@hummingbirdindia.com")
    time.sleep(0.5)
    
    # Fill password
    password_input = page.locator('input[type="password"]')
    password_input.click()
    password_input.fill("Anu@1234")
    time.sleep(0.5)
    
    # Click Sign In
    page.click("button:has-text('Sign In')")
    time.sleep(3)
    
    # After successful login, navigate to tariff page
    # (Login might redirect to dashboard, so we need to explicitly navigate)
    page.goto("https://test-warsoft-v4.hummingbirdindia.com/property/tariff")
    time.sleep(2)
    
    print("✅ Logged in and navigated to Tariff Management page")
    
    # Return logged-in page
    yield page
    
    # Cleanup
    context.close()


@pytest.fixture
def annotated_screenshot(logged_in_page: Page):
    """Fixture providing screenshot capability for tests"""
    return AnnotatedScreenshot(logged_in_page)
