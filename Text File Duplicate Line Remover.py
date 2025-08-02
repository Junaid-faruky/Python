import sys

with open(sys.argv[1], "r") as f:
    seen = set()
    out = []
    for line in f:
        if line not in seen:
            out.append(line)
            seen.add(line)
with open("deduped_" + sys.argv[1], "w") as f:
    f.writelines(out)
print("Deduped file written.")
