import markdown
import sys
from rich.console import Console

console = Console()

if len(sys.argv) != 2:
    print("Usage: python viewer.py file.md")
    sys.exit(1)

with open(sys.argv[1], "r") as f:
    md = f.read()

html = markdown.markdown(md)
# crude: strip tags for terminal
import re
text = re.sub("<[^>]+>", "", html)
console.print(text)
