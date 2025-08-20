from contextlib import contextmanager
import logging
from typing import Any, Generator

logging.basicConfig(level=logging.INFO)

@contextmanager
def smart_resource_manager(
    resource_name: str, 
    setup_args: Any = None, 
    teardown_args: Any = None
) -> Generator[Any, None, None]:
    """A smart context manager with built-in error handling and logging."""
    resource = None
    try:
        logging.info(f"Setting up {resource_name} with args: {setup_args}")
        # Simulate resource setup
        resource = f"{resource_name}_instance"
        yield resource
        logging.info(f"Successfully used {resource_name}")
    
    except Exception as e:
        logging.error(f"Error while using {resource_name}: {e}")
        raise
    
    finally:
        if resource:
            logging.info(f"Tearing down {resource_name} with args: {teardown_args}")

# Usage
with smart_resource_manager("Database", {"host": "localhost"}, {"force": True}) as db:
    print(f"Using resource: {db}")
    # raise ValueError("Simulated error")  # Uncomment to test error handling
