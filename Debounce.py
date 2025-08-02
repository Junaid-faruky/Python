
---

### 11. **Debounce/Throttle Decorator Utility**
```python
import time
from functools import wraps

def throttle(seconds):
    def decorator(f):
        last_called = [0]
        @wraps(f)
        def wrapper(*args, **kwargs):
            now = time.time()
            if now - last_called[0] >= seconds:
                last_called[0] = now
                return f(*args, **kwargs)
        return wrapper
    return decorator

@throttle(2)
def say_hello():
    print("Hello!")

for _ in range(5):
    say_hello()
    time.sleep(1)
