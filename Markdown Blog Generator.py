import markdown
import os

for md in os.listdir("posts"):
    if md.endswith(".md"):
        with open(f"posts/{md}") as f:
            html = markdown.markdown(f.read())
        out = f"site/{md.replace('.md','.html')}"
        os.makedirs("site", exist_ok=True)
        with open(out, "w") as o:
            o.write(f"<html><body>{html}</body></html>")
print("Generated site/")
