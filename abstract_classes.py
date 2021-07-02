from abc import ABC 

class Animal(ABC):

    def __init__(self, name: str):
        self.name = name
        super().__init()
