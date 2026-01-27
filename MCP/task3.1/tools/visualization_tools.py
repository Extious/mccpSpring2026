"""HTML visualization generation tools"""

from pathlib import Path
from typing import Dict, Optional
import json


async def generate_hierarchical_html(
    structure: Dict, 
    output_path: Optional[str] = None,
    base_dir: Optional[Path] = None
) -> Dict:
    """Generate hierarchical HTML visualization"""
    
    if output_path is None:
        output_path = "visual.html"
    
    output_path = Path(output_path)
    
    # Load template
    if base_dir:
        template_path = base_dir / "templates" / "hierarchical.html"
    else:
        template_path = Path(__file__).parent.parent / "templates" / "hierarchical.html"
    
    if template_path.exists():
        with open(template_path, 'r', encoding='utf-8') as f:
            html_template = f.read()
    else:
        # Fallback: generate basic HTML
        html_template = get_basic_hierarchical_template()
    
    # Generate HTML content
    html_content = generate_hierarchical_content(structure, html_template)
    
    # Write to file
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    return {
        "status": "success",
        "output_path": str(output_path),
        "file_size": len(html_content)
    }


async def generate_interconnected_html(
    structure: Dict,
    connections: Dict,
    output_path: Optional[str] = None,
    base_dir: Optional[Path] = None
) -> Dict:
    """Generate interconnected network HTML visualization"""
    
    if output_path is None:
        output_path = "visual_interconnection_text.html"
    
    output_path = Path(output_path)
    
    # Load template
    if base_dir:
        template_path = base_dir / "templates" / "interconnected.html"
    else:
        template_path = Path(__file__).parent.parent / "templates" / "interconnected.html"
    
    if template_path.exists():
        with open(template_path, 'r', encoding='utf-8') as f:
            html_template = f.read()
    else:
        # Fallback: generate basic HTML
        html_template = get_basic_interconnected_template()
    
    # Generate HTML content
    html_content = generate_interconnected_content(structure, connections, html_template)
    
    # Write to file
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    return {
        "status": "success",
        "output_path": str(output_path),
        "file_size": len(html_content)
    }


def generate_hierarchical_content(structure: Dict, template: str) -> str:
    """Generate hierarchical HTML content"""
    
    title = structure.get("title", "Paper Structure")
    author = structure.get("author", "")
    sections = structure.get("sections", [])
    
    # Build sections HTML
    sections_html = ""
    for section in sections:
        sections_html += f"""
        <div class="section level-{section['level']}">
            <h{section['level']} class="section-heading">{section['heading']}</h{section['level']}>
            <p class="section-excerpt">{section.get('text_excerpt', '')}</p>
        """
        
        # Add subsections
        for subsection in section.get("subsections", []):
            sections_html += f"""
            <div class="subsection level-{subsection['level']}">
                <h{subsection['level']} class="subsection-heading">{subsection['heading']}</h{subsection['level']}>
                <p class="subsection-excerpt">{subsection.get('text_excerpt', '')}</p>
            </div>
            """
        
        sections_html += "</div>"
    
    # Replace placeholders
    html = template.replace("{{TITLE}}", title)
    html = html.replace("{{AUTHOR}}", author)
    html = html.replace("{{SECTIONS}}", sections_html)
    
    return html


def generate_interconnected_content(structure: Dict, connections: Dict, template: str) -> str:
    """Generate interconnected HTML content with network visualization"""
    
    title = structure.get("title", "Paper Structure")
    sections = structure.get("sections", [])
    connections_list = connections.get("connections", [])
    
    # Build sections data for JavaScript
    sections_data = json.dumps([
        {
            "id": i,
            "name": section["heading"],
            "text": section.get("text_excerpt", ""),
            "level": section["level"]
        }
        for i, section in enumerate(sections)
    ])
    
    # Build connections data for JavaScript
    connections_data = json.dumps([
        {
            "source": conn["from"],
            "target": conn["to"],
            "type": conn.get("type", "unknown")
        }
        for conn in connections_list
    ])
    
    # Replace placeholders
    html = template.replace("{{TITLE}}", title)
    html = html.replace("{{SECTIONS_DATA}}", sections_data)
    html = html.replace("{{CONNECTIONS_DATA}}", connections_data)
    
    return html


def get_basic_hierarchical_template() -> str:
    """Fallback basic hierarchical template"""
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Paper Structure: {{TITLE}}</title>
    <style>
        body { font-family: Arial, sans-serif; padding: 20px; background: #f5f5f5; }
        .container { max-width: 900px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; }
        h1 { color: #333; border-bottom: 2px solid #667eea; padding-bottom: 10px; }
        .section { margin: 20px 0; padding: 15px; background: #f9f9f9; border-left: 4px solid #667eea; }
        .section-heading { color: #2d3748; margin-bottom: 10px; }
        .section-excerpt { color: #666; font-size: 0.9em; }
        .subsection { margin-left: 30px; margin-top: 10px; padding: 10px; background: #fff; }
    </style>
</head>
<body>
    <div class="container">
        <h1>{{TITLE}}</h1>
        <p><em>{{AUTHOR}}</em></p>
        {{SECTIONS}}
    </div>
</body>
</html>"""


def get_basic_interconnected_template() -> str:
    """Fallback basic interconnected template"""
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Paper Structure: {{TITLE}}</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 0; background: #1a1a2e; color: #eee; }
        .header { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 20px; text-align: center; }
        .main-container { display: flex; min-height: calc(100vh - 100px); }
        .network-panel { flex: 1; padding: 20px; }
        .detail-panel { width: 400px; background: #16213e; padding: 20px; border-left: 1px solid #333; }
        .section-node { padding: 10px; margin: 5px; background: #667eea; border-radius: 5px; cursor: pointer; }
        .section-node:hover { background: #764ba2; }
    </style>
</head>
<body>
    <div class="header">
        <h1>{{TITLE}}</h1>
        <p>Interactive Network Visualization</p>
    </div>
    <div class="main-container">
        <div class="network-panel">
            <div id="network"></div>
        </div>
        <div class="detail-panel">
            <h3>Section Details</h3>
            <div id="details"></div>
        </div>
    </div>
    <script>
        const sections = {{SECTIONS_DATA}};
        const connections = {{CONNECTIONS_DATA}};
        // Network visualization code would go here
        document.getElementById('network').innerHTML = '<p>Network visualization (requires D3.js or similar library)</p>';
    </script>
</body>
</html>"""
