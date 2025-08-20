class ValidatedMeta(type):
    def __new__(cls, name, bases, namespace):
        # Add validation methods for attributes with type hints
        for attr_name, attr_value in namespace.items():
            if isinstance(attr_value, property) and hasattr(attr_value.fget, '__annotations__'):
                return_type = attr_value.fget.__annotations__.get('return')
                if return_type:
                    namespace[f'_validate_{attr_name}'] = cls._create_validator(attr_name, return_type)
        
        return super().__new__(cls, name, bases, namespace)
    
    @staticmethod
    def _create_validator(attr_name, expected_type):
        def validator(self, value):
            if not isinstance(value, expected_type):
                raise TypeError(f"{attr_name} must be {expected_type.__name__}, got {type(value).__name__}")
            return value
        return validator

class Person(metaclass=ValidatedMeta):
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value: str):
        self._name = self._validate_name(value)
    
    @property
    def age(self) -> int:
        return self._age
    
    @age.setter
    def age(self, value: int):
        self._age = self._validate_age(value)

# Usage
p = Person("Alice", 30)
p.name = "Bob"  # Valid
# p.age = "thirty"  # Would raise TypeError
