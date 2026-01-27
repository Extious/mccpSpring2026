"""Paper parsing and structure analysis tools"""

import re
import html
from pathlib import Path
from typing import Dict, List, Optional, Any


async def parse_paper_structure(file_path: Optional[str] = None, file_content: Optional[str] = None) -> Dict:
    """Parse paper structure from LaTeX, PDF, or Markdown"""
    
    if file_content:
        content = file_content
        source = "provided_content"
    elif file_path:
        file_path_obj = Path(file_path).expanduser().resolve()
        if not file_path_obj.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
        
        with open(file_path_obj, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        source = str(file_path_obj)
    else:
        raise ValueError("Either file_path or file_content must be provided")
    
    # Detect format and parse accordingly
    if file_path:
        file_ext = Path(file_path).suffix.lower()
        if file_ext == '.tex':
            return parse_latex_structure(content, source)
        elif file_ext in ['.html', '.htm']:
            return parse_html_structure(content, source)
        elif file_ext in ['.md', '.markdown']:
            return parse_markdown_structure(content, source)
    
    # Try LaTeX parsing by default
    return parse_latex_structure(content, source)


def parse_latex_structure(content: str, source: str) -> Dict:
    """Parse LaTeX document structure"""
    
    # Extract title
    title_match = re.search(r'\\title\{([^}]+)\}', content)
    title = title_match.group(1) if title_match else "Untitled Paper"
    
    # Extract author
    author_match = re.search(r'\\author\{([^}]+)\}', content)
    author = author_match.group(1) if author_match else "Unknown"
    
    # Extract sections
    sections = []
    
    # Pattern for sections: \section{...}, \subsection{...}, etc.
    section_pattern = r'\\(section|subsection|subsubsection|paragraph)\{([^}]+)\}'
    
    current_section = None
    current_subsection = None
    current_subsubsection = None
    
    for match in re.finditer(section_pattern, content):
        level_type = match.group(1)
        heading = match.group(2)
        position = match.start()
        
        # Get text excerpt (next 200 chars after heading)
        excerpt_start = match.end()
        excerpt_end = min(excerpt_start + 200, len(content))
        text_excerpt = content[excerpt_start:excerpt_end].strip()
        text_excerpt = re.sub(r'\s+', ' ', text_excerpt)  # Normalize whitespace
        
        section_data = {
            "level": get_section_level(level_type),
            "heading": heading,
            "text_excerpt": text_excerpt[:150] + "..." if len(text_excerpt) > 150 else text_excerpt,
            "position": position
        }
        
        if level_type == 'section':
            current_section = {
                **section_data,
                "subsections": []
            }
            sections.append(current_section)
            current_subsection = None
            current_subsubsection = None
        
        elif level_type == 'subsection' and current_section:
            current_subsection = {
                **section_data,
                "subsubsections": []
            }
            current_section["subsections"].append(current_subsection)
            current_subsubsection = None
        
        elif level_type == 'subsubsection' and current_subsection:
            current_subsubsection = section_data
            current_subsection["subsubsections"].append(current_subsubsection)
    
    # Extract abstract if present
    abstract_match = re.search(r'\\begin\{abstract\}(.*?)\\end\{abstract\}', content, re.DOTALL)
    abstract = abstract_match.group(1).strip() if abstract_match else None
    
    return {
        "status": "success",
        "source": source,
        "title": title,
        "author": author,
        "abstract": abstract,
        "sections": sections,
        "section_count": len(sections)
    }


def parse_markdown_structure(content: str, source: str) -> Dict:
    """Parse Markdown document structure"""
    
    lines = content.split('\n')
    title = "Untitled Paper"
    sections = []
    
    current_section = None
    
    for i, line in enumerate(lines):
        # Extract title (first # heading)
        if line.startswith('# ') and not title or title == "Untitled Paper":
            title = line[2:].strip()
            continue
        
        # Match headings
        heading_match = re.match(r'^(#{1,4})\s+(.+)$', line)
        if heading_match:
            level = len(heading_match.group(1))
            heading = heading_match.group(2).strip()
            
            # Get text excerpt (next few lines)
            excerpt_lines = []
            for j in range(i + 1, min(i + 5, len(lines))):
                if lines[j].strip() and not lines[j].startswith('#'):
                    excerpt_lines.append(lines[j].strip())
            text_excerpt = ' '.join(excerpt_lines[:3])
            
            section_data = {
                "level": level,
                "heading": heading,
                "text_excerpt": text_excerpt[:150] + "..." if len(text_excerpt) > 150 else text_excerpt,
                "position": i
            }
            
            if level == 1:
                current_section = {
                    **section_data,
                    "subsections": []
                }
                sections.append(current_section)
            elif level == 2 and current_section:
                current_section["subsections"].append(section_data)
    
    return {
        "status": "success",
        "source": source,
        "title": title,
        "sections": sections,
        "section_count": len(sections)
    }


def parse_html_structure(content: str, source: str) -> Dict:
    """Parse HTML document structure"""
    
    # Extract title
    title_match = re.search(r'<title[^>]*>([^<]+)</title>', content, re.IGNORECASE)
    title = title_match.group(1).strip() if title_match else "Untitled Paper"
    
    # Extract h1-h6 headings
    sections = []
    current_section = None
    
    # Pattern for headings: <h1>...</h1>, <h2>...</h2>, etc.
    heading_pattern = r'<h([1-6])[^>]*>(.*?)</h[1-6]>'
    
    for match in re.finditer(heading_pattern, content, re.IGNORECASE | re.DOTALL):
        level = int(match.group(1))
        heading_text = html.unescape(re.sub(r'<[^>]+>', '', match.group(2))).strip()
        
        if not heading_text:
            continue
        
        # Get text excerpt (next 200 chars after heading)
        excerpt_start = match.end()
        excerpt_end = min(excerpt_start + 200, len(content))
        text_excerpt = content[excerpt_start:excerpt_end]
        # Remove HTML tags from excerpt
        text_excerpt = re.sub(r'<[^>]+>', '', text_excerpt).strip()
        text_excerpt = html.unescape(text_excerpt)
        text_excerpt = re.sub(r'\s+', ' ', text_excerpt)
        
        section_data = {
            "level": level,
            "heading": heading_text,
            "text_excerpt": text_excerpt[:150] + "..." if len(text_excerpt) > 150 else text_excerpt,
            "position": match.start()
        }
        
        if level == 1:
            current_section = {
                **section_data,
                "subsections": []
            }
            sections.append(current_section)
        elif level == 2 and current_section:
            current_section["subsections"].append(section_data)
        elif level >= 3 and current_section and current_section.get("subsections"):
            # Add to last subsection
            if current_section["subsections"]:
                current_section["subsections"][-1].setdefault("subsubsections", []).append(section_data)
    
    return {
        "status": "success",
        "source": source,
        "title": title,
        "sections": sections,
        "section_count": len(sections)
    }


def get_section_level(level_type: str) -> int:
    """Convert LaTeX section type to numeric level"""
    level_map = {
        'section': 1,
        'subsection': 2,
        'subsubsection': 3,
        'paragraph': 4
    }
    return level_map.get(level_type, 1)


async def analyze_section_interconnections(structure: Dict, file_path: Optional[str] = None) -> Dict:
    """Analyze relationships between sections"""
    
    sections = structure.get("sections", [])
    connections = []
    
    # Build section index
    section_index = {}
    for i, section in enumerate(sections):
        section_index[section["heading"]] = {
            "index": i,
            "section": section
        }
        for j, subsection in enumerate(section.get("subsections", [])):
            section_index[subsection["heading"]] = {
                "index": (i, j),
                "section": subsection,
                "parent": section["heading"]
            }
    
    # Analyze connections
    for i, section in enumerate(sections):
        # Sequential connection to next section
        if i < len(sections) - 1:
            connections.append({
                "from": section["heading"],
                "to": sections[i + 1]["heading"],
                "type": "sequential",
                "strength": "strong"
            })
        
        # Check for references in text
        text = section.get("text_excerpt", "").lower()
        
        # Look for method/results references
        if "method" in text or "approach" in text:
            for other_section in sections:
                if "method" in other_section["heading"].lower():
                    connections.append({
                        "from": section["heading"],
                        "to": other_section["heading"],
                        "type": "references",
                        "strength": "medium"
                    })
        
        # Check subsections
        for subsection in section.get("subsections", []):
            connections.append({
                "from": section["heading"],
                "to": subsection["heading"],
                "type": "hierarchical",
                "strength": "strong"
            })
    
    return {
        "status": "success",
        "sections": sections,
        "connections": connections,
        "connection_count": len(connections)
    }
