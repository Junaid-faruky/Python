# 12. Regex email validation
import re
print(bool(re.match(r"[^@]+@[^@]+\.[^@]+", "test@mail.com")))
