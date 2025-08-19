# A descriptor class for validating that a value is positive
class PositiveNumber:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError("Value must be positive")
        instance.__dict__[self.name] = value

class Person:
    age = PositiveNumber() # Descriptor instance
    height = PositiveNumber() # Another descriptor instance

    def __init__(self, age, height):
        self.age = age # This calls PositiveNumber.__set__
        self.height = height

p = Person(25, 175)
print(p.age) # Output: 25
# p.age = -10 # This would raise a ValueError
