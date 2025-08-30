from typing import Generic, TypeVar, Optional
import heapq
from collections import deque

T = TypeVar('T')

class SkipNode(Generic[T]):
    def __init__(self, value: T, level: int):
        self.value = value
        self.forward = [None] * (level + 1)

class SkipList(Generic[T]):
    def __init__(self, max_level: int = 16, p: float = 0.5):
        self.max_level = max_level
        self.p = p
        self.header = SkipNode(None, max_level)
        self.level = 0
        self.size = 0
    
    def random_level(self) -> int:
        level = 0
        while random.random() < self.p and level < self.max_level:
            level += 1
        return level
    
    def insert(self, value: T):
        update = [None] * (self.max_level + 1)
        current = self.header
        
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current
        
        current = current.forward[0]
        
        if current is None or current.value != value:
            new_level = self.random_level()
            
            if new_level > self.level:
                for i in range(self.level + 1, new_level + 1):
                    update[i] = self.header
                self.level = new_level
            
            new_node = SkipNode(value, new_level)
            
            for i in range(new_level + 1):
                new_node.forward[i] = update[i].forward[i]
                update[i].forward[i] = new_node
            
            self.size += 1
    
    def search(self, value: T) -> bool:
        current = self.header
        
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
        
        current = current.forward[0]
        return current is not None and current.value == value

class BloomFilter:
    def __init__(self, size: int, hash_count: int = 3):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = [False] * size
    
    def _hashes(self, item: str) -> List[int]:
        return [hash(f"{item}{i}") % self.size for i in range(self.hash_count)]
    
    def add(self, item: str):
        for index in self._hashes(item):
            self.bit_array[index] = True
    
    def contains(self, item: str) -> bool:
        return all(self.bit_array[index] for index in self._hashes(item))

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
    
    def search(self, word: str) -> bool:
        node = self.root
