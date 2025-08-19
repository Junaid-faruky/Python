from dataclasses import dataclass
from typing import List

# Without a dataclass (lots of boilerplate)
class OldPerson:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"
    def __eq__(self, other):
        return (self.name, self.age) == (other.name, other.age)

# With a dataclass (clean and concise)
@dataclass
class Person:
    name: str
    age: int
    hobbies: List[str] = None # Default value
    active: bool = True # Another default value

# __init__, __repr__, and __eq__ are auto-generated!
person1 = Person("Alice", 30, ["coding"])
person2 = Person("Alice", 30)
print(person1) # Output: Person(name='Alice', age=30, hobbies=['coding'], active=True)
print(person1 == person2) # Output: False (because hobbies are different)
