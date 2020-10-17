#Python:     3.8.5
#Author:     Nicholas Mireles
#Assignment: Polymorphism

class Shape:
    def __init__(self,name):
        self.name = name

    def area(self):
        pass

    def formula(self):
        return "How to calculate the area of various shapes."

    def __str__(self):
        return self.name

class Circle(Shape):
    def __init__(self, radius, pi):
        super().__init__("Circle")
        self.radius = radius
        self.pi = pi

    def formula(self):
        return "Pi times the radius squared is the formula used to find the area of a circle."

    def area(self):
        return self.pi*self.radius**2

class Rectangle(Shape):
    def __init__(self,width,length):
        super().__init__("Rectangle")
        self.width = width
        self.length = length

    def formula(self):
        return "Length times width is the formula used to find the area of a rectangle."

    def area(self):
        return self.length*self.width

    

if __name__ == "__main__":
    
    r = Rectangle(3,6)
    print(r)
    print(r.formula())
    print(r.area())
    
    c = Circle(5, 3.14)
    print(c)
    print(c.formula())
    print(c.area())
    
    
    
    
