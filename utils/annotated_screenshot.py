"""
Annotated Screenshot Helper
Creates meaningful bug screenshots with:
- Cursor/pointer highlighting
- Bounding boxes around elements
- Text annotations
- Arrows pointing to issues
"""

from PIL import Image, ImageDraw, ImageFont
import os
from datetime import datetime
from playwright.sync_api import Page, Locator


class AnnotatedScreenshotHelper:
    """Helper class to create annotated bug screenshots"""
    
    def __init__(self, page: Page, output_dir: str = "assets/bugs_annotated"):
        self.page = page
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        
    def capture_with_cursor(self, filename: str, cursor_x: int = None, cursor_y: int = None, 
                           cursor_size: int = 30):
        """
        Take screenshot and add cursor at specified position
        If cursor position not provided, uses current mouse position
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filepath = os.path.join(self.output_dir, f"{filename}_{timestamp}.png")
        
        # Take base screenshot
        self.page.screenshot(path=filepath, full_page=True)
        
        # Add cursor if coordinates provided
        if cursor_x is not None and cursor_y is not None:
            img = Image.open(filepath)
            draw = ImageDraw.Draw(img)
            
            # Draw cursor (triangle pointer)
            cursor_points = [
                (cursor_x, cursor_y),  # Top point
                (cursor_x - cursor_size//2, cursor_y + cursor_size),  # Bottom left
                (cursor_x + cursor_size//2, cursor_y + cursor_size),  # Bottom right
            ]
            draw.polygon(cursor_points, fill='red', outline='white')
            
            # Draw circle at tip for emphasis
            circle_radius = 5
            draw.ellipse(
                [(cursor_x - circle_radius, cursor_y - circle_radius),
                 (cursor_x + circle_radius, cursor_y + circle_radius)],
                fill='yellow', outline='red'
            )
            
            img.save(filepath)
        
        print(f"📸 Annotated screenshot: {filepath}")
        return filepath
    
    def capture_element_with_box(self, filename: str, element: Locator, 
                                 label: str = "", box_color: str = "red"):
        """
        Capture screenshot and draw bounding box around element
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filepath = os.path.join(self.output_dir, f"{filename}_{timestamp}.png")
        
        # Take base screenshot
        self.page.screenshot(path=filepath, full_page=True)
        
        try:
            # Get element bounding box
            box = element.bounding_box()
            if box:
                img = Image.open(filepath)
                draw = ImageDraw.Draw(img)
                
                # Draw rectangle around element
                rect = [
                    (box['x'] - 5, box['y'] - 5),
                    (box['x'] + box['width'] + 5, box['y'] + box['height'] + 5)
                ]
                
                # Convert color name to RGB
                color_map = {
                    'red': (255, 0, 0),
                    'green': (0, 255, 0),
                    'blue': (0, 0, 255),
                    'yellow': (255, 255, 0),
                    'orange': (255, 165, 0)
                }
                color = color_map.get(box_color.lower(), (255, 0, 0))
                
                # Draw thick rectangle
                for i in range(4):
                    draw.rectangle(
                        [(rect[0][0] + i, rect[0][1] + i),
                         (rect[1][0] - i, rect[1][1] - i)],
                        outline=color
                    )
                
                # Add label if provided
                if label:
                    try:
                        # Try to use a larger font
                        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 20)
                    except:
                        font = ImageFont.load_default()
                    
                    # Draw label background
                    text_bbox = draw.textbbox((0, 0), label, font=font)
                    text_width = text_bbox[2] - text_bbox[0]
                    text_height = text_bbox[3] - text_bbox[1]
                    
                    label_bg = [
                        (box['x'] - 5, box['y'] - text_height - 15),
                        (box['x'] + text_width + 10, box['y'] - 5)
                    ]
                    draw.rectangle(label_bg, fill=color)
                    
                    # Draw label text
                    draw.text(
                        (box['x'], box['y'] - text_height - 10),
                        label,
                        fill='white',
                        font=font
                    )
                
                # Add cursor pointing to element
                cursor_x = int(box['x'] + box['width'] // 2)
                cursor_y = int(box['y'] - 40)
                
                # Draw arrow cursor pointing down to element
                arrow_points = [
                    (cursor_x, cursor_y + 30),  # Bottom point (pointing to element)
                    (cursor_x - 15, cursor_y),  # Top left
                    (cursor_x + 15, cursor_y),  # Top right
                ]
                draw.polygon(arrow_points, fill='red', outline='white')
                
                img.save(filepath)
        except Exception as e:
            print(f"⚠️  Could not add annotation: {e}")
        
        print(f"📸 Annotated screenshot with box: {filepath}")
        return filepath
    
    def capture_with_multiple_boxes(self, filename: str, elements_with_labels: list):
        """
        Capture screenshot with multiple annotated elements
        elements_with_labels: [(element, label, color), ...]
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filepath = os.path.join(self.output_dir, f"{filename}_{timestamp}.png")
        
        # Take base screenshot
        self.page.screenshot(path=filepath, full_page=True)
        
        try:
            img = Image.open(filepath)
            draw = ImageDraw.Draw(img)
            
            try:
                font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 18)
            except:
                font = ImageFont.load_default()
            
            color_map = {
                'red': (255, 0, 0),
                'green': (0, 255, 0),
                'blue': (0, 0, 255),
                'yellow': (255, 255, 0),
                'orange': (255, 165, 0)
            }
            
            for element, label, color in elements_with_labels:
                try:
                    box = element.bounding_box()
                    if not box:
                        continue
                    
                    rgb_color = color_map.get(color.lower(), (255, 0, 0))
                    
                    # Draw rectangle
                    rect = [
                        (box['x'] - 3, box['y'] - 3),
                        (box['x'] + box['width'] + 3, box['y'] + box['height'] + 3)
                    ]
                    
                    for i in range(3):
                        draw.rectangle(
                            [(rect[0][0] + i, rect[0][1] + i),
                             (rect[1][0] - i, rect[1][1] - i)],
                            outline=rgb_color
                        )
                    
                    # Draw label
                    if label:
                        text_bbox = draw.textbbox((0, 0), label, font=font)
                        text_width = text_bbox[2] - text_bbox[0]
                        text_height = text_bbox[3] - text_bbox[1]
                        
                        label_bg = [
                            (box['x'] - 3, box['y'] - text_height - 12),
                            (box['x'] + text_width + 8, box['y'] - 3)
                        ]
                        draw.rectangle(label_bg, fill=rgb_color)
                        draw.text(
                            (box['x'], box['y'] - text_height - 8),
                            label,
                            fill='white',
                            font=font
                        )
                except:
                    continue
            
            img.save(filepath)
        except Exception as e:
            print(f"⚠️  Could not add annotations: {e}")
        
        print(f"📸 Annotated screenshot with multiple boxes: {filepath}")
        return filepath
    
    def capture_error_state(self, filename: str, error_message: str = ""):
        """
        Capture current page state as error with big error label
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filepath = os.path.join(self.output_dir, f"{filename}_{timestamp}.png")
        
        self.page.screenshot(path=filepath, full_page=True)
        
        if error_message:
            try:
                img = Image.open(filepath)
                draw = ImageDraw.Draw(img)
                
                try:
                    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 30)
                except:
                    font = ImageFont.load_default()
                
                # Draw error banner at top
                banner_height = 60
                draw.rectangle([(0, 0), (img.width, banner_height)], fill=(255, 0, 0))
                draw.text((20, 15), f"❌ BUG: {error_message}", fill='white', font=font)
                
                img.save(filepath)
            except Exception as e:
                print(f"⚠️  Could not add error banner: {e}")
        
        print(f"📸 Error screenshot: {filepath}")
        return filepath
