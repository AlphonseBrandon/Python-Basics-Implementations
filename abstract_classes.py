from abc import ABC, abstractmethod 

class Animal(ABC):

    def __init__(self, name: str):
        self.name = name
        super().__init()

    @abstractmethod
    def make_sound(self):
        pass

    
