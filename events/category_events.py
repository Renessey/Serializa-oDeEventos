from datetime import datetime

class CategoryEvent:
    def __init__(self, category_id: str, timestamp: datetime):
        self.category_id = category_id
        self.timestamp = timestamp

class CategoryCreated(CategoryEvent):
    pass

class CategoryUpdated(CategoryEvent):
    def __init__(self, category_id: str, timestamp: datetime, changed_fields: dict):
        super().__init__(category_id, timestamp)
        self.changed_fields = changed_fields

class CategoryActivated(CategoryEvent):
    pass

class CategoryDeactivated(CategoryEvent):
    pass
