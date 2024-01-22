class Rectangle:
    def __init__(self,lenght,width):
        self.lenght=lenght
        self.width=width

class Cube(Rectangle):
    def __init__(self,lenght,width):
       super().__init__(lenght,width)

    def volume(self):
        return self.lenght*self.width

class Square(Rectangle):
    def __init__(self,lenght,width,height):
       super().__init__(lenght,width)
       self.height=height
     
    def volume(self):
        return self.lenght*self.width*self.height
    
cube=Cube(3,3)
square=Square(3,3,3)
print(cube.volume())
print(square.volume())