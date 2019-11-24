class Pokemon:
    def __init__(self, id: int, name: str, height: int, weight: int, order: int):
        self.id = id
        self.name = name
        self.height = height
        self.weight = weight
        self.order = order

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'height': self.height,
            'weight': self.weight,
            'order': self.order
        }