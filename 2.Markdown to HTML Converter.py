import markdown

with open("notes.md", "r") as f:
    md_content = f.read()

html_content = markdown.markdown(md_content)
with open("notes.html", "w") as f:
    f.write(html_content)

print("Converted Markdown to HTML!")
