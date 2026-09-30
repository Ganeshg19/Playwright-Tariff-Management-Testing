"""
Screenshot Annotation Utility
Annotates bug screenshots with visual markers to highlight issues
"""

from PIL import Image, ImageDraw, ImageFont
import os
from pathlib import Path

class BugAnnotator:
    """Annotate screenshots to highlight bugs"""
    
    def __init__(self):
        self.colors = {
            'red': '#FF0000',
            'orange': '#FF6600',
            'yellow': '#FFFF00',
            'green': '#00FF00',
            'blue': '#0000FF',
            'white': '#FFFFFF',
            'black': '#000000'
        }
        
        # Try to load a font, fallback to default
        try:
            self.font_large = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 40)
            self.font_medium = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 30)
            self.font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
        except:
            self.font_large = ImageFont.load_default()
            self.font_medium = ImageFont.load_default()
            self.font_small = ImageFont.load_default()
    
    def draw_rectangle(self, image, coords, color='red', thickness=5):
        """Draw a rectangle to highlight an area"""
        draw = ImageDraw.Draw(image)
        x, y, width, height = coords
        draw.rectangle(
            [(x, y), (x + width, y + height)],
            outline=self.colors[color],
            width=thickness
        )
        return image
    
    def draw_circle(self, image, coords, color='red', thickness=5):
        """Draw a circle to highlight an area"""
        draw = ImageDraw.Draw(image)
        x, y, radius = coords
        draw.ellipse(
            [(x - radius, y - radius), (x + radius, y + radius)],
            outline=self.colors[color],
            width=thickness
        )
        return image
    
    def draw_arrow(self, image, start, end, color='red', thickness=5):
        """Draw an arrow pointing to the bug"""
        draw = ImageDraw.Draw(image)
        x1, y1 = start
        x2, y2 = end
        
        # Draw line
        draw.line([(x1, y1), (x2, y2)], fill=self.colors[color], width=thickness)
        
        # Draw arrowhead
        arrow_size = 20
        import math
        angle = math.atan2(y2 - y1, x2 - x1)
        
        # Left side of arrowhead
        x3 = x2 - arrow_size * math.cos(angle - math.pi / 6)
        y3 = y2 - arrow_size * math.sin(angle - math.pi / 6)
        
        # Right side of arrowhead
        x4 = x2 - arrow_size * math.cos(angle + math.pi / 6)
        y4 = y2 - arrow_size * math.sin(angle + math.pi / 6)
        
        draw.polygon([(x2, y2), (x3, y3), (x4, y4)], fill=self.colors[color])
        
        return image
    
    def add_text(self, image, text, position, color='red', font_size='medium', background=True):
        """Add text annotation"""
        draw = ImageDraw.Draw(image)
        x, y = position
        
        font = self.font_medium
        if font_size == 'large':
            font = self.font_large
        elif font_size == 'small':
            font = self.font_small
        
        # Add background for better readability
        if background:
            # Get text bounding box
            bbox = draw.textbbox((x, y), text, font=font)
            padding = 10
            draw.rectangle(
                [(bbox[0] - padding, bbox[1] - padding), 
                 (bbox[2] + padding, bbox[3] + padding)],
                fill=self.colors['white'],
                outline=self.colors[color],
                width=3
            )
        
        # Draw text
        draw.text((x, y), text, fill=self.colors[color], font=font)
        
        return image
    
    def add_banner(self, image, text, position='top'):
        """Add a banner with bug description"""
        draw = ImageDraw.Draw(image)
        width, height = image.size
        
        banner_height = 80
        if position == 'top':
            y = 0
        else:
            y = height - banner_height
        
        # Draw banner background
        draw.rectangle(
            [(0, y), (width, y + banner_height)],
            fill=self.colors['red'],
            outline=self.colors['black'],
            width=3
        )
        
        # Draw text
        text_x = 20
        text_y = y + 20
        draw.text((text_x, text_y), text, fill=self.colors['white'], font=self.font_medium)
        
        return image
    
    def annotate_bug(self, image_path, output_path, annotations):
        """
        Annotate a screenshot with bug markers
        
        annotations = {
            'banner': 'BUG #1: Checkbox not clearly visible',
            'rectangles': [{'coords': (100, 200, 300, 150), 'color': 'red'}],
            'circles': [{'coords': (500, 300, 50), 'color': 'orange'}],
            'arrows': [{'start': (100, 100), 'end': (200, 200), 'color': 'red'}],
            'texts': [{'text': 'Checkbox hidden', 'position': (150, 150), 'color': 'red'}]
        }
        """
        # Open image
        image = Image.open(image_path)
        
        # Add banner if provided
        if 'banner' in annotations:
            image = self.add_banner(image, annotations['banner'])
        
        # Draw rectangles
        if 'rectangles' in annotations:
            for rect in annotations['rectangles']:
                image = self.draw_rectangle(
                    image, 
                    rect['coords'], 
                    rect.get('color', 'red'),
                    rect.get('thickness', 5)
                )
        
        # Draw circles
        if 'circles' in annotations:
            for circle in annotations['circles']:
                image = self.draw_circle(
                    image,
                    circle['coords'],
                    circle.get('color', 'red'),
                    circle.get('thickness', 5)
                )
        
        # Draw arrows
        if 'arrows' in annotations:
            for arrow in annotations['arrows']:
                image = self.draw_arrow(
                    image,
                    arrow['start'],
                    arrow['end'],
                    arrow.get('color', 'red'),
                    arrow.get('thickness', 5)
                )
        
        # Add text labels
        if 'texts' in annotations:
            for text_info in annotations['texts']:
                image = self.add_text(
                    image,
                    text_info['text'],
                    text_info['position'],
                    text_info.get('color', 'red'),
                    text_info.get('font_size', 'medium')
                )
        
        # Save annotated image
        image.save(output_path, quality=95)
        print(f"✅ Annotated: {output_path}")
        return output_path


# Example usage
if __name__ == "__main__":
    annotator = BugAnnotator()
    
    # Example annotation
    annotations = {
        'banner': 'BUG #1: Checkbox not clearly visible',
        'rectangles': [
            {'coords': (100, 200, 300, 50), 'color': 'red'}
        ],
        'texts': [
            {'text': 'Checkbox is too small', 'position': (120, 180), 'color': 'red'}
        ],
        'arrows': [
            {'start': (50, 150), 'end': (100, 220), 'color': 'red'}
        ]
    }
    
    print("Bug Annotator utility ready!")
    print("Use annotator.annotate_bug(image_path, output_path, annotations)")
