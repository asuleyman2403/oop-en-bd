class Rectangle:
    def __init__(self, a, b):
        self.width = a
        self.length = b
        self.area = a * b
    
    # getter method
    def get_width(self):
        return self.width

    # setter method
    def set_width(self, width):
        self.width = width

    def get_length(self):
        return self.length

    def set_length(self, length):
        self.length = length

    def get_area(self):
        return self.area
    
    def set_area(self, area):
        self.area = area

rectangle = Rectangle(4, 5)
print(rectangle.get_width())
print(rectangle.get_length())
print(rectangle.get_area())

# THE ISSUE WITH AREA WITH PUBLIC METHOD
rectangle.width = 5
print(rectangle.get_width())
print(rectangle.get_length())
print(rectangle.get_area())

