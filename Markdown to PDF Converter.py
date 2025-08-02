import subprocess
import sys

md_file = sys.argv[1]
pdf_file = md_file.replace(".md", ".pdf")
subprocess.run(["pandoc", md_file, "-o", pdf_file])
print(f"Converted {md_file} to {pdf_file}")
