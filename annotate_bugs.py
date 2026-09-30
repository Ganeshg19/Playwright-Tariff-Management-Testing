"""
Batch Annotate Existing Bug Screenshots
Run this script to annotate all existing bug screenshots
"""

import os
import sys
from pathlib import Path
import glob

# Add utils to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'utils'))

from utils.bug_annotator import BugAnnotator
from utils.bug_annotation_config import BUG_ANNOTATIONS


def annotate_existing_screenshots():
    """Annotate all existing bug screenshots"""
    
    annotator = BugAnnotator()
    
    # Directories
    bugs_dir = "assets/bugs"
    annotated_dir = "assets/bugs_annotated"
    
    # Create annotated directory
    os.makedirs(annotated_dir, exist_ok=True)
    
    # Get all bug screenshots
    screenshot_files = glob.glob(os.path.join(bugs_dir, "bug_*.png"))
    
    print(f"\n📸 Found {len(screenshot_files)} bug screenshots to annotate\n")
    
    annotated_count = 0
    skipped_count = 0
    
    for screenshot_path in sorted(screenshot_files):
        filename = os.path.basename(screenshot_path)
        
        # Extract bug name (e.g., 'bug_01_checkbox_not_visible' from 'bug_01_checkbox_not_visible_20260929_162039.png')
        parts = filename.split('_')
        
        # Try different patterns to match bug name
        bug_patterns = [
            f"{parts[0]}_{parts[1]}_{parts[2]}",  # bug_01_checkbox
            f"{parts[0]}_{parts[1]}_{parts[2]}_{parts[3]}",  # bug_01_checkbox_not
            f"{parts[0]}_{parts[1]}_{parts[2]}_{parts[3]}_{parts[4]}",  # Full name
        ]
        
        bug_name = None
        for pattern in bug_patterns:
            if pattern in BUG_ANNOTATIONS:
                bug_name = pattern
                break
        
        if not bug_name:
            print(f"⚠️  Skipped (no annotation config): {filename}")
            skipped_count += 1
            continue
        
        # Generate output filename
        output_filename = filename.replace('.png', '_ANNOTATED.png')
        output_path = os.path.join(annotated_dir, output_filename)
        
        # Skip if already annotated
        if os.path.exists(output_path):
            print(f"⏭️  Already annotated: {output_filename}")
            continue
        
        try:
            # Annotate
            annotator.annotate_bug(
                image_path=screenshot_path,
                output_path=output_path,
                annotations=BUG_ANNOTATIONS[bug_name]
            )
            annotated_count += 1
            
        except Exception as e:
            print(f"❌ Error annotating {filename}: {e}")
    
    print(f"\n" + "="*60)
    print(f"✅ Successfully annotated: {annotated_count} screenshots")
    print(f"⚠️  Skipped (no config): {skipped_count} screenshots")
    print(f"📁 Annotated screenshots saved to: {annotated_dir}/")
    print("="*60 + "\n")
    
    # Generate index HTML
    generate_comparison_html(bugs_dir, annotated_dir)


def generate_comparison_html(bugs_dir, annotated_dir):
    """Generate HTML page to compare original and annotated screenshots"""
    
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bug Screenshots - Before & After Annotation</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: #f5f5f5;
            padding: 20px;
        }
        h1 {
            text-align: center;
            color: #333;
            margin-bottom: 30px;
            padding: 20px;
            background: white;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        .comparison-grid {
            display: grid;
            gap: 30px;
            max-width: 1800px;
            margin: 0 auto;
        }
        .bug-comparison {
            background: white;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 2px 15px rgba(0,0,0,0.1);
        }
        .bug-title {
            font-size: 1.3em;
            font-weight: bold;
            color: #d32f2f;
            margin-bottom: 15px;
            padding-bottom: 10px;
            border-bottom: 3px solid #d32f2f;
        }
        .images-container {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
        }
        .image-section {
            text-align: center;
        }
        .image-label {
            font-weight: bold;
            margin-bottom: 10px;
            padding: 8px;
            border-radius: 5px;
        }
        .original-label {
            background: #ff9800;
            color: white;
        }
        .annotated-label {
            background: #4caf50;
            color: white;
        }
        img {
            max-width: 100%;
            height: auto;
            border: 2px solid #ddd;
            border-radius: 5px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            cursor: zoom-in;
        }
        img:hover {
            transform: scale(1.02);
            transition: transform 0.3s;
        }
        .stats {
            text-align: center;
            background: white;
            padding: 20px;
            margin-bottom: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        .stats span {
            display: inline-block;
            margin: 0 20px;
            font-size: 1.2em;
        }
        .legend {
            background: #fff3cd;
            padding: 15px;
            border-left: 4px solid #ff9800;
            margin-bottom: 30px;
            border-radius: 5px;
        }
        .legend h3 {
            color: #856404;
            margin-bottom: 10px;
        }
        .legend ul {
            list-style: none;
            padding-left: 20px;
        }
        .legend li {
            margin: 5px 0;
        }
        .modal {
            display: none;
            position: fixed;
            z-index: 1000;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.9);
            cursor: zoom-out;
        }
        .modal img {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            max-width: 95%;
            max-height: 95%;
            cursor: zoom-out;
        }
    </style>
    <script>
        function openModal(imgSrc) {
            const modal = document.getElementById('imageModal');
            const modalImg = document.getElementById('modalImage');
            modal.style.display = 'block';
            modalImg.src = imgSrc;
        }
        
        function closeModal() {
            document.getElementById('imageModal').style.display = 'none';
        }
    </script>
</head>
<body>
    <h1>🐛 Bug Screenshots - Original vs Annotated</h1>
    
    <div class="stats">
        <span>📸 Total Bugs: <strong id="bugCount">0</strong></span>
        <span>✏️ Annotated: <strong id="annotatedCount">0</strong></span>
    </div>
    
    <div class="legend">
        <h3>📝 Annotation Legend</h3>
        <ul>
            <li>🔴 <strong>Red Rectangle/Circle:</strong> Main bug location</li>
            <li>🟠 <strong>Orange:</strong> Secondary issues or warnings</li>
            <li>🟢 <strong>Green Text:</strong> Expected/correct behavior</li>
            <li>➡️ <strong>Arrows:</strong> Point to specific problem areas</li>
            <li>📋 <strong>Top Banner:</strong> Bug ID and description</li>
        </ul>
    </div>
    
    <div class="comparison-grid" id="comparisonGrid">
        <!-- Bug comparisons will be inserted here -->
    </div>
    
    <!-- Modal for full-size image view -->
    <div id="imageModal" class="modal" onclick="closeModal()">
        <img id="modalImage" src="">
    </div>
    
    <script>
        // Bug data will be inserted here
        const bugData = [
"""
    
    # Find all annotated screenshots
    annotated_files = glob.glob(os.path.join(annotated_dir, "*_ANNOTATED.png"))
    bug_data = []
    
    for annotated_path in sorted(annotated_files):
        annotated_filename = os.path.basename(annotated_path)
        original_filename = annotated_filename.replace('_ANNOTATED', '')
        original_path = os.path.join(bugs_dir, original_filename)
        
        if os.path.exists(original_path):
            # Extract bug name
            parts = original_filename.replace('.png', '').split('_')
            bug_id = f"{parts[0]}_{parts[1]}"  # bug_01, bug_02, etc.
            bug_name = '_'.join(parts[:5]) if len(parts) >= 5 else '_'.join(parts[:4])
            
            bug_data.append({
                'id': bug_id.upper(),
                'name': bug_name.replace('_', ' ').title(),
                'original': f"../{original_path}",
                'annotated': f"../{annotated_path}"
            })
    
    # Add bug data to HTML
    for bug in bug_data:
        html_content += f"""
            {{
                id: "{bug['id']}",
                name: "{bug['name']}",
                original: "{bug['original']}",
                annotated: "{bug['annotated']}"
            }},
"""
    
    html_content += """
        ];
        
        // Populate the page
        document.getElementById('bugCount').textContent = bugData.length;
        document.getElementById('annotatedCount').textContent = bugData.length;
        
        const grid = document.getElementById('comparisonGrid');
        
        bugData.forEach(bug => {
            const bugDiv = document.createElement('div');
            bugDiv.className = 'bug-comparison';
            bugDiv.innerHTML = `
                <div class="bug-title">${bug.id}: ${bug.name}</div>
                <div class="images-container">
                    <div class="image-section">
                        <div class="image-label original-label">📸 Original Screenshot</div>
                        <img src="${bug.original}" alt="${bug.id} Original" onclick="openModal('${bug.original}')">
                    </div>
                    <div class="image-section">
                        <div class="image-label annotated-label">✏️ Annotated (Bug Highlighted)</div>
                        <img src="${bug.annotated}" alt="${bug.id} Annotated" onclick="openModal('${bug.annotated}')">
                    </div>
                </div>
            `;
            grid.appendChild(bugDiv);
        });
    </script>
</body>
</html>
"""
    
    # Save HTML file
    html_path = "bug_screenshots_comparison.html"
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"\n📄 Comparison HTML generated: {html_path}")
    print(f"   Open this file in a browser to view all bug screenshots!\n")


if __name__ == "__main__":
    print("\n" + "="*60)
    print("🎨 Bug Screenshot Annotator")
    print("="*60)
    annotate_existing_screenshots()
