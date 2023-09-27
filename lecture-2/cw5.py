class Rectangle:
    def __init__(self, a, b):
        self._width = a
        self._length = b
        self._area = a * b

    # getter method
    def get_width(self):
        return self._width

    # setter method
    def set_width(self, width):
        self._width = width
        self.calcalute_area()

    def get_length(self):
        return self._length

    def set_length(self, length):
        self._length = length

    def get_area(self):
        return self._width * self._length

rectangle = Rectangle(4, 5)
# # 3 * 5 = 15
# rectangle.width = 4
# # 4, 5, 15
print(rectangle.get_width())
print(rectangle.get_length())
print(rectangle.get_area())

rectangle.set_width(5)
print(rectangle.get_width())
print(rectangle.get_length())
print(rectangle.get_area())
