class Rectangle:
    def __init__(self, a, b):
        self.__width = a
        self.__length = b
    
    # getter method
    def get_width(self):
        return self.__width

    # setter method
    def set_width(self, width):
        self.__width = width

    def get_length(self):
        return self.__length

    def set_length(self, length):
        self.__length = length

rectangle = Rectangle(4, 5)

# BAD
rectangle.__width = 5

print(rectangle.get_width())
print(rectangle.get_length())


