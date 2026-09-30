"""
Demo Test: Visual Cursor Movement
Shows how to use the visual cursor during test execution
"""

import pytest
from playwright.sync_api import Page
import time
import sys
import os

# Add utils to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))
from visual_cursor import VisualCursor, enable_visual_cursor


class TestVisualCursorDemo:
    """Demo tests showing visual cursor in action"""
    
    def test_01_visual_cursor_property_selection(self, logged_in_page: Page):
        """
        Demo: Property selection with visual cursor
        Watch the RED cursor move and click!
        """
        # Create visual cursor (RED color, 30px size)
        cursor = VisualCursor(logged_in_page, cursor_size=30, cursor_color="red")
        
        print("\n🎯 Starting Visual Cursor Demo...")
        time.sleep(1)
        
        # Step 1: Move to property search input
        print("📍 Step 1: Moving to property search input...")
        property_input = logged_in_page.locator("input[placeholder*='Property']").first
        cursor.move_to_element(property_input, duration=0.8)
        time.sleep(0.5)
        
        # Step 2: Click with cursor animation
        print("📍 Step 2: Clicking property input...")
        cursor.click_with_cursor(property_input, duration=0.6)
        
        # Step 3: Type with cursor visible
        print("📍 Step 3: Typing 'AM Property'...")
        property_input.type("AM Property", delay=150)
        time.sleep(2)
        
        # Step 4: Move to dropdown option and click
        print("📍 Step 4: Selecting from dropdown...")
        dropdown_items = logged_in_page.locator("[role='option']").all()
        if dropdown_items:
            cursor.click_with_cursor(dropdown_items[0], duration=0.6)
        
        time.sleep(2)
        print("✅ Visual cursor demo complete!")
    
    def test_02_visual_cursor_edit_button(self, logged_in_page: Page):
        """
        Demo: Click Edit button with visual cursor
        """
        cursor = VisualCursor(logged_in_page, cursor_size=35, cursor_color="#FF0000")
        
        # Select property first
        property_input = logged_in_page.locator("input[placeholder*='Property']").first
        cursor.click_with_cursor(property_input, duration=0.5)
        property_input.type("AM Property", delay=100)
        time.sleep(2)
        
        dropdown = logged_in_page.locator("[role='option']").first
        cursor.click_with_cursor(dropdown, duration=0.5)
        time.sleep(3)
        
        # Find and click Edit button with cursor
        print("\n📍 Looking for Edit button...")
        edit_buttons = logged_in_page.locator("button:has-text('Edit'), [title='Edit']").all()
        
        if edit_buttons:
            print(f"✅ Found {len(edit_buttons)} edit buttons")
            print("📍 Moving cursor to first Edit button...")
            
            # Hover first
            cursor.hover_with_cursor(edit_buttons[0], duration=0.8)
            time.sleep(0.5)
            
            # Then click
            print("📍 Clicking Edit button...")
            cursor.click_with_cursor(edit_buttons[0], duration=0.6)
            time.sleep(2)
            
            # Modal should open - move cursor to center
            print("📍 Modal opened! Moving cursor to center...")
            cursor.move_to(960, 540, duration=0.8)
            time.sleep(1)
            
            # Close modal
            print("📍 Closing modal...")
            logged_in_page.keyboard.press("Escape")
            time.sleep(1)
    
    def test_03_visual_cursor_add_room_charges(self, logged_in_page: Page):
        """
        Demo: Complete Add Room Charges flow with visual cursor
        """
        # Use ORANGE cursor for this test
        cursor = VisualCursor(logged_in_page, cursor_size=40, cursor_color="orange")
        
        print("\n🎯 Starting Add Room Charges visual demo...")
        
        # Select property
        property_input = logged_in_page.locator("input[placeholder*='Property']").first
        cursor.click_with_cursor(property_input, duration=0.5)
        property_input.type("AM", delay=150)
        time.sleep(2)
        
        dropdown = logged_in_page.locator("[role='option']").first
        cursor.click_with_cursor(dropdown, duration=0.5)
        time.sleep(3)
        
        # Find Add Room Charges button
        print("📍 Looking for 'Add Room Charges' button...")
        add_button = logged_in_page.locator("button:has-text('Add Room Charges')").first
        
        if add_button.is_visible():
            print("✅ Found Add button")
            
            # Move cursor to button (with slow animation)
            print("📍 Moving cursor to Add button (watch the movement!)...")
            cursor.move_to_element(add_button, duration=1.0)
            time.sleep(0.5)
            
            # Click with animation
            print("📍 Clicking Add Room Charges...")
            cursor.click_with_cursor(add_button, duration=0.8)
            time.sleep(2)
            
            # Modal should open
            print("✅ Add Room Charges dialog opened!")
            
            # Move cursor around to show modal elements
            print("📍 Exploring modal elements...")
            cursor.move_to(512, 300, duration=0.6)
            time.sleep(0.5)
            cursor.move_to(700, 400, duration=0.6)
            time.sleep(0.5)
            cursor.move_to(512, 500, duration=0.6)
            time.sleep(0.5)
            
            # Close
            print("📍 Closing modal...")
            logged_in_page.keyboard.press("Escape")
            time.sleep(1)
    
    def test_04_cursor_color_demo(self, logged_in_page: Page):
        """
        Demo: Different cursor colors
        """
        colors = ["red", "blue", "green", "purple", "orange"]
        
        for i, color in enumerate(colors):
            print(f"\n🎨 Demo {i+1}: {color.upper()} cursor")
            cursor = VisualCursor(logged_in_page, cursor_size=30, cursor_color=color)
            
            # Move cursor in a pattern
            positions = [
                (400, 300),
                (600, 300),
                (600, 500),
                (400, 500),
                (400, 300),
            ]
            
            for x, y in positions:
                cursor.move_to(x, y, duration=0.3)
                time.sleep(0.2)
            
            cursor.remove_cursor()
            time.sleep(0.5)
    
    def test_05_cursor_with_form_filling(self, logged_in_page: Page):
        """
        Demo: Cursor movement while filling a form
        """
        cursor = VisualCursor(logged_in_page, cursor_size=30, cursor_color="red")
        
        # Select property
        property_input = logged_in_page.locator("input[placeholder*='Property']").first
        cursor.type_with_cursor(property_input, "AM Property")
        time.sleep(2)
        
        # Select from dropdown
        dropdown = logged_in_page.locator("[role='option']").first
        cursor.click_with_cursor(dropdown, duration=0.5)
        time.sleep(2)
        
        # Open Edit dialog
        edit_button = logged_in_page.locator("button:has-text('Edit')").first
        if edit_button.is_visible():
            cursor.click_with_cursor(edit_button, duration=0.5)
            time.sleep(2)
            
            # Get all input fields in modal
            modal = logged_in_page.locator("[role='dialog']").first
            inputs = modal.locator("input:not([type='hidden'])").all()
            
            print(f"\n✅ Found {len(inputs)} input fields")
            
            # Move cursor to each input (showcase)
            for i, inp in enumerate(inputs[:5]):  # First 5 inputs
                print(f"📍 Moving to input {i+1}...")
                cursor.move_to_element(inp, duration=0.5)
                time.sleep(0.3)
            
            # Close modal
            logged_in_page.keyboard.press("Escape")
            time.sleep(1)
