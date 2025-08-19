import asyncio

async def fetch_data(delay, name):
    """Simulate a slow I/O operation (e.g., a network request)."""
    print(f"Fetching data from {name}...")
    await asyncio.sleep(delay) # This is the non-blocking sleep
    print(f"Data received from {name}!")
    return f"data from {name}"

async def main():
    # Schedule both coroutines to run concurrently
    task1 = asyncio.create_task(fetch_data(2, 'Server A'))
    task2 = asyncio.create_task(fetch_data(1, 'Server B'))

    # Wait for both tasks to complete and get their results
    result1 = await task1
    result2 = await task2
    print(f"All done: {result1}, {result2}")

# Run the main coroutine
asyncio.run(main())
# Output order will demonstrate concurrency:
# Fetching data from Server A...
# Fetching data from Server B...
# Data received from Server B! (finishes first due to shorter delay)
# Data received from Server A!
# All done: data from Server A, data from Server B
