from contextlib import contextmanager, AbstractContextManager
from typing import List, Generator, Optional
import threading
import time
from dataclasses import dataclass
from queue import Queue, Empty

@dataclass
class DatabaseConnection:
    id: int
    is_connected: bool = False
    
    def connect(self):
        print(f"Connection {self.id} connecting...")
        time.sleep(0.1)  # Simulate connection time
        self.is_connected = True
        print(f"Connection {self.id} connected")
    
    def disconnect(self):
        print(f"Connection {self.id} disconnecting...")
        self.is_connected = False
        print(f"Connection {self.id} disconnected")
    
    def execute(self, query: str):
        if not self.is_connected:
            raise RuntimeError("Connection not established")
        print(f"Connection {self.id} executing: {query}")
        return f"Result from {self.id} for {query}"

class ConnectionPool:
    def __init__(self, size: int = 3):
        self.size = size
        self._pool: Queue[DatabaseConnection] = Queue()
        self._lock = threading.Lock()
        self._initialize_pool()
    
    def _initialize_pool(self):
        for i in range(self.size):
            conn = DatabaseConnection(i + 1)
            conn.connect()
            self._pool.put(conn)
    
    @contextmanager
    def get_connection(self, timeout: float = 5.0) -> Generator[DatabaseConnection, None, None]:
        try:
            with self._lock:
                conn = self._pool.get(timeout=timeout)
            yield conn
        except Empty:
            raise TimeoutError("No connections available")
        finally:
            if 'conn' in locals():
                self._pool.put(conn)
    
    def close_all(self):
        while not self._pool.empty():
            try:
                conn = self._pool.get_nowait()
                conn.disconnect()
            except Empty:
                break

# Usage
pool = ConnectionPool(size=2)

def worker(worker_id: int, query: str):
    try:
        with pool.get_connection() as conn:
            result = conn.execute(f"{query} by worker {worker_id}")
            time.sleep(1)  # Simulate work
            print(f"Worker {worker_id} got: {result}")
    except Exception as e:
        print(f"Worker {worker_id} failed: {e}")

# Simulate concurrent access
threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i, f"SELECT * FROM table_{i}"))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

pool.close_all()
