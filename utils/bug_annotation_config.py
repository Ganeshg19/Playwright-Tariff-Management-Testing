"""
Bug Annotation Configuration
Defines where and how to annotate each bug screenshot
"""

BUG_ANNOTATIONS = {
    # Bug #1: Checkbox not clearly visible
    "bug_01_checkbox_not_visible": {
        "banner": "BUG #1: TAC Exceptions Checkbox Not Clearly Visible",
        "description": "Checkbox UI element is hard to see - needs better contrast/size",
        "rectangles": [
            {"coords": (50, 200, 400, 100), "color": "red", "thickness": 5}
        ],
        "texts": [
            {"text": "❌ Checkbox barely visible", "position": (60, 150), "color": "red", "font_size": "medium"},
            {"text": "→ Needs larger size + better contrast", "position": (60, 320), "color": "orange"}
        ],
        "arrows": [
            {"start": (30, 180), "end": (70, 240), "color": "red"}
        ]
    },
    
    # Bug #2: Control initial space in filter
    "bug_02_filter_initial_space": {
        "banner": "BUG #2: Filter Allows Initial Space (Should Be Trimmed)",
        "description": "Filter input accepts leading spaces which should be prevented",
        "rectangles": [
            {"coords": (100, 150, 500, 60), "color": "red"}
        ],
        "texts": [
            {"text": "❌ Accepts: ' test' (with leading space)", "position": (120, 100), "color": "red"},
            {"text": "✅ Should only accept: 'test'", "position": (120, 230), "color": "green"}
        ],
        "circles": [
            {"coords": (115, 180, 30), "color": "red"}
        ]
    },
    
    # Bug #3: Table header name is in caps
    "bug_03_table_header_caps": {
        "banner": "BUG #3: Table Headers in ALL CAPS (Should Be Title Case)",
        "description": "Table headers are in uppercase, should follow proper title case",
        "rectangles": [
            {"coords": (50, 250, 1800, 60), "color": "red"}
        ],
        "texts": [
            {"text": "❌ ALL CAPS", "position": (200, 200), "color": "red"},
            {"text": "✅ Should be: 'Property Name', 'Valid From', etc.", "position": (200, 330), "color": "green"}
        ]
    },
    
    # Bug #4: Table heading name difference
    "bug_04_table_heading_mismatch": {
        "banner": "BUG #4: Table Header Name Different from Old Site",
        "description": "New site uses different header names - inconsistent with legacy",
        "rectangles": [
            {"coords": (400, 250, 300, 60), "color": "red"}
        ],
        "texts": [
            {"text": "⚠️  Header name changed from old site", "position": (420, 200), "color": "orange"}
        ]
    },
    
    # Bug #5: Tool tip data not showing
    "bug_05_tooltip_missing": {
        "banner": "BUG #5: Tax Inclusive Tooltip Not Showing on Hover",
        "description": "Hovering over 'Tax Inclusive' field should show tooltip",
        "circles": [
            {"coords": (500, 400, 60), "color": "red"}
        ],
        "texts": [
            {"text": "❌ No tooltip appears", "position": (550, 350), "color": "red"},
            {"text": "✅ Should show: 'Tax Inclusive - explanation...'", "position": (550, 470), "color": "green"}
        ],
        "arrows": [
            {"start": (600, 380), "end": (520, 400), "color": "red"}
        ]
    },
    
    # Bug #6: Design issue at background
    "bug_06_design_background": {
        "banner": "BUG #6: Background Design Issue When Modal Opens",
        "description": "Background elements visible/overlapping when popup appears",
        "rectangles": [
            {"coords": (100, 100, 1700, 900), "color": "orange", "thickness": 8}
        ],
        "texts": [
            {"text": "⚠️  Background not properly dimmed", "position": (150, 50), "color": "orange"},
            {"text": "Modal overlay issue", "position": (150, 1000), "color": "red"}
        ]
    },
    
    # Bug #7: Error message content
    "bug_07_error_message": {
        "banner": "BUG #7: Error Message Content Unclear/Confusing",
        "description": "Error message doesn't clearly explain what went wrong",
        "rectangles": [
            {"coords": (300, 400, 800, 100), "color": "red"}
        ],
        "texts": [
            {"text": "❌ Unclear error message", "position": (320, 350), "color": "red"},
            {"text": "Example: 'Use Existing image from grid'", "position": (320, 520), "color": "orange"},
            {"text": "→ Where is the grid? How to use?", "position": (320, 560), "color": "red"}
        ]
    },
    
    # Bug #8: Date picker icon alignment
    "bug_08_date_picker_alignment": {
        "banner": "BUG #8: Date Picker Icon Alignment Issue",
        "description": "Calendar icon not properly aligned in center",
        "circles": [
            {"coords": (850, 350, 40), "color": "red"}
        ],
        "texts": [
            {"text": "❌ Icon misaligned", "position": (900, 320), "color": "red"},
            {"text": "Should be centered", "position": (900, 400), "color": "green"}
        ],
        "arrows": [
            {"start": (900, 350), "end": (870, 350), "color": "red"}
        ]
    },
    
    # Bug #9: Room image upload size not fit to the box
    "bug_09_room_image_fit": {
        "banner": "BUG #9: Room Image Upload Doesn't Fit Box Properly",
        "description": "Uploaded image overflows or doesn't fill the designated area",
        "rectangles": [
            {"coords": (200, 300, 300, 250), "color": "red"}
        ],
        "texts": [
            {"text": "❌ Image doesn't fit", "position": (520, 350), "color": "red"},
            {"text": "Overflowing/gaps visible", "position": (520, 400), "color": "orange"}
        ],
        "arrows": [
            {"start": (510, 370), "end": (350, 370), "color": "red"}
        ]
    },
    
    # Bug #10: Alignment issue - single, double, triple
    "bug_10_alignment_issue": {
        "banner": "BUG #10: Single/Double/Triple Occupancy Alignment Not Centered",
        "description": "Occupancy type fields are not properly aligned in center",
        "rectangles": [
            {"coords": (600, 400, 700, 80), "color": "red"}
        ],
        "texts": [
            {"text": "❌ Not centered", "position": (620, 350), "color": "red"},
            {"text": "↕️ Should be vertically aligned", "position": (620, 500), "color": "green"}
        ]
    },
    
    # Bug #11: Tool tip not shown in Room charge details table
    "bug_11_tooltip_room_charge": {
        "banner": "BUG #11: Tooltips Missing on Edit/Delete Icons",
        "description": "No tooltips appear when hovering over action icons",
        "circles": [
            {"coords": (1650, 450, 50), "color": "red"},
            {"coords": (1720, 450, 50), "color": "red"}
        ],
        "texts": [
            {"text": "❌ No tooltip on Edit icon", "position": (1550, 380), "color": "red"},
            {"text": "❌ No tooltip on Delete icon", "position": (1550, 530), "color": "red"}
        ]
    },
    
    # Bug #12: To Date captured wrongly in screen
    "bug_12_to_date_wrong": {
        "banner": "BUG #12: To Date Display Wrong (DB=13/03/2026, Screen=28/02/2027)",
        "description": "Date shown in UI doesn't match database value",
        "rectangles": [
            {"coords": (800, 400, 250, 60), "color": "red", "thickness": 6}
        ],
        "texts": [
            {"text": "❌ Showing: 28/02/2027", "position": (820, 350), "color": "red"},
            {"text": "✅ Should be: 13/03/2026", "position": (820, 480), "color": "green"},
            {"text": "⚠️  UI-DB mismatch!", "position": (820, 520), "color": "orange"}
        ]
    },
    
    # Bug #13: Tariff fields amount able to enter more
    "bug_13_tariff_length": {
        "banner": "BUG #13: Tariff Amount Field Has No Length Validation",
        "description": "Can enter unlimited digits - should have max length constraint",
        "rectangles": [
            {"coords": (600, 350, 300, 60), "color": "red"}
        ],
        "texts": [
            {"text": "❌ Accepts: 999999999999999...", "position": (620, 300), "color": "red"},
            {"text": "✅ Should limit to: 10 digits max", "position": (620, 430), "color": "green"}
        ]
    },
    
    # Bug #14: Remove pagination in Room charge Details
    "bug_14_pagination": {
        "banner": "BUG #14: Unnecessary Pagination (Only 3 Rows)",
        "description": "Pagination controls shown even with few rows",
        "rectangles": [
            {"coords": (700, 750, 500, 60), "color": "orange"}
        ],
        "texts": [
            {"text": "⚠️  Pagination not needed for < 10 rows", "position": (720, 700), "color": "orange"}
        ],
        "circles": [
            {"coords": (950, 780, 100), "color": "red"}
        ]
    },
    
    # Bug #15: TAC Percentage dot not allowing issue
    "bug_15_tac_percentage_dot": {
        "banner": "BUG #15: TAC Percentage Field Doesn't Accept Decimal Point",
        "description": "Decimal values like '12.5' are not accepted",
        "rectangles": [
            {"coords": (500, 400, 250, 60), "color": "red"}
        ],
        "texts": [
            {"text": "❌ Can't enter: 12.5", "position": (520, 350), "color": "red"},
            {"text": "✅ Should accept decimal values", "position": (520, 480), "color": "green"}
        ]
    },
    
    # Bug #16: Date manually allowing to edit
    "bug_16_date_manual_edit": {
        "banner": "BUG #16: Date Field Allows Manual Typing (Should Be Picker Only)",
        "description": "Users can type invalid dates manually - should use picker only",
        "rectangles": [
            {"coords": (400, 350, 300, 60), "color": "red"}
        ],
        "texts": [
            {"text": "❌ Can type: 99/99/9999", "position": (420, 300), "color": "red"},
            {"text": "✅ Should be readonly/picker only", "position": (420, 430), "color": "green"}
        ]
    },
    
    # Bug #17: Filter not cleared after property name selected
    "bug_17_filter_not_cleared": {
        "banner": "BUG #17: Filter Text Persists After Property Selection",
        "description": "Filter should auto-clear when property is selected",
        "rectangles": [
            {"coords": (100, 150, 400, 60), "color": "orange"},
            {"coords": (600, 150, 400, 60), "color": "red"}
        ],
        "texts": [
            {"text": "1️⃣  Filter entered", "position": (120, 100), "color": "orange"},
            {"text": "2️⃣  Property selected", "position": (620, 100), "color": "red"},
            {"text": "❌ Filter still visible", "position": (120, 230), "color": "red"},
            {"text": "✅ Should auto-clear", "position": (620, 230), "color": "green"}
        ]
    },
    
    # Bug #18: Design overlaps
    "bug_18_design_overlaps": {
        "banner": "BUG #18: Column Headers Overlap When Scrolling Horizontally",
        "description": "Headers overlap/stack when user scrolls horizontally",
        "rectangles": [
            {"coords": (800, 200, 400, 80), "color": "red", "thickness": 6}
        ],
        "texts": [
            {"text": "❌ Headers overlapping", "position": (820, 150), "color": "red"},
            {"text": "→ Scroll right to see issue", "position": (820, 300), "color": "orange"}
        ]
    },
    
    # Bug #19: Design issue in Firefox browser
    "bug_19_firefox_design": {
        "banner": "BUG #19: Firefox-Specific Design/Layout Issue",
        "description": "Layout breaks or renders differently in Firefox",
        "rectangles": [
            {"coords": (100, 100, 1700, 900), "color": "orange", "thickness": 10}
        ],
        "texts": [
            {"text": "⚠️  FIREFOX ONLY BUG", "position": (150, 50), "color": "red", "font_size": "large"},
            {"text": "Layout/styling issue specific to Firefox browser", "position": (150, 1000), "color": "orange"}
        ]
    },
    
    # Bug #20: Room image upload inside the box - Text issue
    "bug_20_room_image_text": {
        "banner": "BUG #20: 'Room' Text Overlapping Uploaded Image",
        "description": "Text label appears over/inside image upload area",
        "rectangles": [
            {"coords": (200, 300, 300, 250), "color": "red"}
        ],
        "texts": [
            {"text": "❌ Text overlapping image", "position": (520, 350), "color": "red"},
            {"text": "'Room' label visible over image", "position": (520, 400), "color": "orange"}
        ],
        "circles": [
            {"coords": (250, 350, 40), "color": "red"}
        ]
    },
    
    # Additional bugs (21-42)
    "bug_21_property_required_validation": {
        "banner": "BUG #21: Property Name Required - Validation Message Position",
        "description": "Validation message for required field appears in wrong position",
        "texts": [
            {"text": "⚠️  Validation message positioning issue", "position": (100, 200), "color": "orange"}
        ]
    },
    
    "bug_22_no_records_styling": {
        "banner": "BUG #22: 'No Records Found' Message Styling/Alignment",
        "description": "Empty state message not properly styled or centered",
        "texts": [
            {"text": "❌ Message not centered/styled properly", "position": (100, 400), "color": "red"}
        ]
    }
}


# Coordinates are approximate - adjust based on actual screenshot dimensions
# Format: (x, y, width, height) for rectangles
#         (x, y, radius) for circles
#         (x1, y1), (x2, y2) for arrows
