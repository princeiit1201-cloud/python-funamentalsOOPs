from abc import ABC, abstractmethod

class enforce(ABC):
    @abstractmethod
    def enginestart():
        pass

class bike(enforce):
    def enginestart():
        pass

    
class car(enforce):
    def enginestart():
        pass

class truck(enforce):
    def enginestart():
        pass

obj1 = bike() # creating an object of the class
obj2 = car() # creating an object of the class
obj3 = truck() # creating an object of the class

