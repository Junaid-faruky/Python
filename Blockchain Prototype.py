import hashlib
import time

class Block:
    def __init__(self, index, prev_hash, data, nonce=0):
        self.index = index
        self.prev_hash = prev_hash
        self.data = data
        self.nonce = nonce
        self.timestamp = time.time()

    def hash(self):
        s = f"{self.index}{self.prev_hash}{self.data}{self.nonce}{self.timestamp}"
        return hashlib.sha256(s.encode()).hexdigest()

def mine(block, difficulty=4):
    prefix = "0" * difficulty
    while not block.hash().startswith(prefix):
        block.nonce += 1
    return block

genesis = Block(0, "0", "Genesis")
mined = mine(genesis)
print("Mined hash:", mined.hash())
