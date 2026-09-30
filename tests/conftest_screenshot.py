"""
Enhanced Screenshot Helper with Automatic Annotation
"""

import pytest
from playwright.sync_api import Page
from datetime import datetime
import os
import sys

# Add utils to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))

from bug_annotator import BugAnnotator
from bug_annotation_config import BUG_ANNOTATIONS


class AnnotatedScreenshot:
    """Helper class for taking and annotating bug screenshots"""
    
    def __init__(self, page: Page):
        self.page = page
        self.annotator = BugAnnotator()
        self.screenshots_dir = "assets/screenshots"
        self.bugs_dir = "assets/bugs"
        self.annotated_dir = "assets/bugs_annotated"
        
        # Create directories
        for dir_path in [self.screenshots_dir, self.bugs_dir, self.annotated_dir]:
            os.makedirs(dir_path, exist_ok=True)
    
    def capture_bug(self, bug_name: str, auto_annotate: bool = True):
        """
        Capture screenshot and optionally annotate it
        
        Args:
            bug_name: Name of the bug (e.g., 'bug_01_checkbox_not_visible')
            auto_annotate: Whether to automatically annotate the screenshot
        
        Returns:
            tuple: (original_path, annotated_path)
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Take original screenshot
        original_filename = f"{bug_name}_{timestamp}.png"
        original_path = os.path.join(self.bugs_dir, original_filename)
        self.page.screenshot(path=original_path, full_page=True)
        print(f"📸 Screenshot saved: {original_path}")
        
        # Annotate if enabled and config exists
        annotated_path = None
        if auto_annotate and bug_name in BUG_ANNOTATIONS:
            annotated_filename = f"{bug_name}_ANNOTATED_{timestamp}.png"
            annotated_path = os.path.join(self.annotated_dir, annotated_filename)
            
            try:
                self.annotator.annotate_bug(
                    image_path=original_path,
                    output_path=annotated_path,
                    annotations=BUG_ANNOTATIONS[bug_name]
                )
                print(f"✏️  Annotated: {annotated_path}")
            except Exception as e:
                print(f"⚠️  Annotation failed: {e}")
                annotated_path = None
        
        return original_path, annotated_path
    
    def capture_element_bug(self, bug_name: str, element_selector: str, auto_annotate: bool = True):
        """Capture specific element screenshot"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        original_filename = f"{bug_name}_element_{timestamp}.png"
        original_path = os.path.join(self.bugs_dir, original_filename)
        
        element = self.page.locator(element_selector)
        element.screenshot(path=original_path)
        print(f"📸 Element screenshot: {original_path}")
        
        return original_path


@pytest.fixture
def annotated_screenshot(logged_in_page: Page):
    """Fixture providing annotated screenshot capability"""
    return AnnotatedScreenshot(logged_in_page)


# Example usage in tests:
"""
def test_bug_example(annotated_screenshot):
    '''Test with automatic annotation'''
    # Navigate and prepare state
    # ...
    
    # Capture and annotate automatically
    original, annotated = annotated_screenshot.capture_bug(
        bug_name='bug_01_checkbox_not_visible',
        auto_annotate=True
    )
    
    # Both screenshots are saved:
    # - Original: assets/bugs/bug_01_checkbox_not_visible_20260929_120000.png
    # - Annotated: assets/bugs_annotated/bug_01_checkbox_not_visible_ANNOTATED_20260929_120000.png
"""
