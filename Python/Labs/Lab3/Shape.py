from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self):
        print("I am a shape")
    
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass




 