#Python:     3.9.0
#Author:     Nicholas Mireles
#Assignment: Abstraction Assignment

from abc import ABC, abstractmethod

class Shapes(ABC):
    def sides(self):
        print('How many sides does a ')
    @abstractmethod
    def num(self):
        pass

class Triangle(Shapes):
    def num(self):
        print('triangle have?: 3')
        
class Hex(Shapes):
    def num(self):
        print('hexagon have?: 6')
    



if __name__ == "__main__":
     obj = Triangle()
     obj.sides()
     obj.num()

     obj = Hex()
     obj.sides()
     obj.num()
     
     
     
