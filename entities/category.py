from dataclasses import dataclass, field
from typing import List, Dict
from datetime import datetime
from events.category_events import (
    CategoryCreated,
    CategoryUpdated,
    CategoryActivated,
    CategoryDeactivated
)
import uuid

@dataclass
class Category:
    id: str
    name: str
    description: str = ""
    is_active: bool = True
    events: List = field(default_factory=list)

    def __post_init__(self):
        if not self.id:
            self.id = str(uuid.uuid4())
        # Registra evento de criação
        self.events.append(CategoryCreated(self.id, datetime.now()))

    # -------------------
    # Métodos de atualização
    # -------------------
    def update(self, name: str = None, description: str = None):
        old_values = {"name": self.name, "description": self.description}
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        changed_fields = {k: v for k, v in old_values.items() if getattr(self, k) != v}
        if changed_fields:
            self.events.append(CategoryUpdated(self.id, datetime.now(), changed_fields))

    def activate(self):
        if not self.is_active:
            self.is_active = True
            self.events.append(CategoryActivated(self.id, datetime.now()))

    def deactivate(self):
        if self.is_active:
            self.is_active = False
            self.events.append(CategoryDeactivated(self.id, datetime.now()))

    # -------------------
    # Serialização
    # -------------------
    def to_dict(self) -> Dict:
        return {
            "class_name": self.__class__.__name__,
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "is_active": self.is_active
        }

    @classmethod
    def from_dict(cls, data: Dict):
        return cls(
            id=data.get("id"),
            name=data.get("name"),
            description=data.get("description", ""),
            is_active=data.get("is_active", True)
        )
