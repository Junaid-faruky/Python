import markdown
from pathlib import Path

md_text = Path("notes.md").read_text()
html = markdown.markdown(md_text)
Path("notes.html").write_text(html)
print("Converted notes.md to notes.html")
