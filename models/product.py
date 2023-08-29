import json

class Product:
    def __init__(self):
        self.title: str = ""
        self.images: list[str] = []
        self.description: str = ""
        self.price: int = 0

    def __str__(self):
        return json.dumps(self.__dict__)
