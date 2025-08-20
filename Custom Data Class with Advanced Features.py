from dataclasses import dataclass, field, asdict
from typing import List, Dict, Any, ClassVar
from datetime import datetime
import json

@dataclass
class AdvancedUser:
    name: str
    email: str
    created_at: datetime = field(default_factory=datetime.now)
    metadata: Dict[str, Any] = field(default_factory=dict)
    tags: List[str] = field(default_factory=list)
    
    # Class variable
    user_count: ClassVar[int] = 0
    
    def __post_init__(self):
        AdvancedUser.user_count += 1
        if not self.validate_email():
            raise ValueError("Invalid email format")
    
    def validate_email(self) -> bool:
        return '@' in self.email and '.' in self.email.split('@')[1]
    
    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)
    
    def to_json(self) -> str:
        data = asdict(self)
        data['created_at'] = self.created_at.isoformat()
        return json.dumps(data)
    
    @classmethod
    def from_json(cls, json_str: str) -> 'AdvancedUser':
        data = json.loads(json_str)
        data['created_at'] = datetime.fromisoformat(data['created_at'])
        return cls(**data)
    
    def __str__(self) -> str:
        return f"User(name={self.name}, email={self.email}, tags={len(self.tags)})"

# Usage
user = AdvancedUser("John Doe", "john@example.com")
user.add_tag("premium")
user.add_tag("active")
print(user.to_json())
