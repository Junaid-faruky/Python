import subprocess
import re
import sys

msg = sys.argv[1]
if len(msg) > 72:
    print("Error: commit message too long (max 72 chars).")
    sys.exit(1)
if not re.match(r"^[A-Z].*", msg):
    print("Error: commit message should start with capital letter.")
    sys.exit(1)
print("Commit message looks good.")
