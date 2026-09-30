"""
Visual Cursor Helper for Playwright Tests
Shows animated cursor movement during test execution for better understanding
"""

from playwright.sync_api import Page
import time


class VisualCursor:
    """Helper class to show visible cursor during test execution"""
    
    def __init__(self, page: Page, cursor_size: int = 30, cursor_color: str = "red"):
        self.page = page
        self.cursor_size = cursor_size
        self.cursor_color = cursor_color
        self.cursor_injected = False
    
    def inject_cursor(self):
        """Inject a visible cursor element into the page"""
        if self.cursor_injected:
            return
        
        # Build HTML separately to avoid f-string issues with CSS
        self.page.evaluate("""
            (args) => {
                const cursorSize = args.size;
                const cursorColor = args.color;
                
                const cursorHTML = `
                    <div id="playwright-cursor" style="
                        position: fixed;
                        width: ${cursorSize}px;
                        height: ${cursorSize}px;
                        border-radius: 50%;
                        background: ${cursorColor};
                        border: 3px solid white;
                        box-shadow: 0 0 10px rgba(0,0,0,0.5);
                        pointer-events: none;
                        z-index: 999999;
                        transition: all 0.15s ease-out;
                        transform: translate(-50%, -50%);
                        display: none;
                    ">
                        <div style="
                            position: absolute;
                            top: 50%;
                            left: 50%;
                            width: 8px;
                            height: 8px;
                            background: white;
                            border-radius: 50%;
                            transform: translate(-50%, -50%);
                        "></div>
                    </div>
                `;
                
                const styleHTML = `
                    <style id="playwright-cursor-style">
                        @keyframes cursor-pulse {
                            0%, 100% { transform: translate(-50%, -50%) scale(1); }
                            50% { transform: translate(-50%, -50%) scale(1.2); }
                        }
                        
                        #playwright-cursor.clicking {
                            animation: cursor-pulse 0.3s ease-in-out;
                            background: orange !important;
                        }
                        
                        #playwright-cursor.hovering {
                            background: yellow !important;
                        }
                    </style>
                `;
                
                // Add cursor element
                const cursorDiv = document.createElement('div');
                cursorDiv.innerHTML = cursorHTML;
                document.body.appendChild(cursorDiv.firstElementChild);
                
                // Add styles
                const styleDiv = document.createElement('div');
                styleDiv.innerHTML = styleHTML;
                document.head.appendChild(styleDiv.firstElementChild);
            }
        """, {"size": self.cursor_size, "color": self.cursor_color})
        
        self.cursor_injected = True
        print("✅ Visual cursor injected")
    
    def move_to(self, x: int, y: int, duration: float = 0.3):
        """Move cursor to specific coordinates with animation"""
        self.inject_cursor()
        
        # Show cursor
        self.page.evaluate("document.getElementById('playwright-cursor').style.display = 'block'")
        
        # Move cursor
        self.page.evaluate("""
            (args) => {
                const cursor = document.getElementById('playwright-cursor');
                cursor.style.left = args.x + 'px';
                cursor.style.top = args.y + 'px';
            }
        """, {"x": x, "y": y})
        
        time.sleep(duration)
    
    def move_to_element(self, locator, duration: float = 0.3):
        """Move cursor to center of element"""
        self.inject_cursor()
        
        try:
            box = locator.bounding_box()
            if box:
                center_x = box['x'] + box['width'] / 2
                center_y = box['y'] + box['height'] / 2
                self.move_to(int(center_x), int(center_y), duration)
        except Exception as e:
            print(f"⚠️  Could not move cursor to element: {e}")
    
    def click_with_cursor(self, locator, duration: float = 0.5):
        """Move cursor to element and click with visual feedback"""
        self.inject_cursor()
        
        try:
            # Get element position
            box = locator.bounding_box()
            if not box:
                print("⚠️  Element not visible, clicking without cursor animation")
                locator.click()
                return
            
            center_x = box['x'] + box['width'] / 2
            center_y = box['y'] + box['height'] / 2
            
            # Move cursor to element
            self.move_to(int(center_x), int(center_y), duration * 0.6)
            
            # Add clicking visual effect
            self.page.evaluate("""
                document.getElementById('playwright-cursor').classList.add('clicking')
            """)
            
            # Perform actual click
            locator.click(force=True)
            
            # Wait for click animation
            time.sleep(duration * 0.4)
            
            # Remove clicking effect
            self.page.evaluate("""
                document.getElementById('playwright-cursor').classList.remove('clicking')
            """)
            
            print(f"✅ Clicked at ({int(center_x)}, {int(center_y)})")
            
        except Exception as e:
            print(f"⚠️  Error during cursor click: {e}")
            # Fallback to regular click
            locator.click()
    
    def hover_with_cursor(self, locator, duration: float = 0.5):
        """Move cursor to element and hover"""
        self.inject_cursor()
        
        try:
            box = locator.bounding_box()
            if box:
                center_x = box['x'] + box['width'] / 2
                center_y = box['y'] + box['height'] / 2
                
                # Move cursor
                self.move_to(int(center_x), int(center_y), duration)
                
                # Add hover effect
                self.page.evaluate("""
                    document.getElementById('playwright-cursor').classList.add('hovering')
                """)
                
                # Perform hover
                locator.hover()
                
                time.sleep(0.3)
                
                # Remove hover effect
                self.page.evaluate("""
                    document.getElementById('playwright-cursor').classList.remove('hovering')
                """)
                
        except Exception as e:
            print(f"⚠️  Error during cursor hover: {e}")
            locator.hover()
    
    def type_with_cursor(self, locator, text: str, delay: int = 100):
        """Click element with cursor, then type"""
        self.click_with_cursor(locator, duration=0.3)
        time.sleep(0.2)
        locator.type(text, delay=delay)
        print(f"✅ Typed: {text}")
    
    def hide_cursor(self):
        """Hide the cursor"""
        if self.cursor_injected:
            self.page.evaluate("""
                document.getElementById('playwright-cursor').style.display = 'none'
            """)
    
    def show_cursor(self):
        """Show the cursor"""
        if self.cursor_injected:
            self.page.evaluate("""
                document.getElementById('playwright-cursor').style.display = 'block'
            """)
    
    def remove_cursor(self):
        """Remove cursor from page"""
        if self.cursor_injected:
            self.page.evaluate("""
                const cursor = document.getElementById('playwright-cursor');
                if (cursor) cursor.remove();
            """)
            self.cursor_injected = False


# Convenience functions for quick usage
def enable_visual_cursor(page: Page, color: str = "red", size: int = 30) -> VisualCursor:
    """Quick setup: Enable visual cursor on a page"""
    cursor = VisualCursor(page, cursor_size=size, cursor_color=color)
    cursor.inject_cursor()
    return cursor


def click_with_visual_cursor(page: Page, locator, duration: float = 0.5):
    """Quick click with cursor animation"""
    cursor = VisualCursor(page)
    cursor.click_with_cursor(locator, duration)
