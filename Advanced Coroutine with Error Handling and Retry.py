import asyncio
from typing import Callable, TypeVar, Any
import random
from functools import wraps

T = TypeVar('T')

class AsyncRetry:
    def __init__(self, max_retries: int = 3, delay: float = 1.0, backoff: float = 2.0):
        self.max_retries = max_retries
        self.delay = delay
        self.backoff = backoff
    
    def __call__(self, coro_func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(coro_func)
        async def wrapper(*args, **kwargs):
            retries = 0
            current_delay = self.delay
            
            while retries <= self.max_retries:
                try:
                    return await coro_func(*args, **kwargs)
                except Exception as e:
                    retries += 1
                    if retries > self.max_retries:
                        print(f"Max retries exceeded. Last error: {e}")
                        raise
                    
                    jitter = random.uniform(0.5, 1.5)
                    wait_time = current_delay * jitter
                    print(f"Retry {retries}/{self.max_retries} after {wait_time:.2f}s. Error: {e}")
                    
                    await asyncio.sleep(wait_time)
                    current_delay *= self.backoff
        
        return wrapper

@AsyncRetry(max_retries=3, delay=1, backoff=2)
async def unreliable_api_call(endpoint: str) -> dict:
    """Simulate an unreliable API call"""
    if random.random() < 0.7:  # 70% chance of failure
        raise ConnectionError(f"Failed to connect to {endpoint}")
    
    return {"status": "success", "data": f"from {endpoint}"}

async def main():
    try:
        result = await unreliable_api_call("/api/users")
        print(f"Success: {result}")
    except Exception as e:
        print(f"Final failure: {e}")

# Run the example
asyncio.run(main())
