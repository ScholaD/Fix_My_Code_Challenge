#!/usr/bin/python3

class Square:
    
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        # Set default values for width and height
        self.width = kwargs.get('width', 0)
        self.height = kwargs.get('height', 0)

    def area_of_my_square(self):
        """Area of the square"""
        return self.width * self.width

    def PerimeterOfMySquare(self):
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print("Area of my square:", s.area_of_my_square())
    print("Perimeter of my square:", s.PerimeterOfMySquare())
