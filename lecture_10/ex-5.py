def check_positive_number(a):
    if a > 0:
        return True
    else:
        raise Exception

def calculate_rectangle_perimeter(a, b):
    if check_positive_number(a) and check_positive_number(b):
        return 2 * a + 2 * b
    return 0


p1 = calculate_rectangle_perimeter(10, 5)
print(p1)

try:
    p2 = calculate_rectangle_perimeter(-10, 0)
except:
    print('Invalid sides of rectangle')





