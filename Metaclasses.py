# A simple metaclass that ensures all class attributes are in uppercase
class UpperCaseMeta(type):
    def __new__(cls, name, bases, dct):
        uppercase_attrs = {}
        for attr_name, attr_value in dct.items():
            if not attr_name.startswith('__'):
                uppercase_attrs[attr_name.upper()] = attr_value
            else:
                uppercase_attrs[attr_name] = attr_value
        return super().__new__(cls, name, bases, uppercase_attrs)

# Using the metaclass (Python 3 syntax)
class MyClass(metaclass=UpperCaseMeta):
    x = 1
    y = 2

    def my_method(self):
        print("Method called")

obj = MyClass()
print(obj.X) # Output: 1 (note the uppercase 'X')
print(hasattr(obj, 'x')) # Output: False
obj.MY_METHOD() # Output: "Method called"
