a = 10

# You can raise any system or custom exception to handle some cases
# if a > 5:
#     raise ZeroDivisionError

def get_exception_fn(a):
    if a > 5:
        return ZeroDivisionError

# Exception is not raised, it is just returned as result of function
b = get_exception_fn(a)
print(b)

def raise_exception_fn(a):
    if a > 5:
        raise ZeroDivisionError

print(raise_exception_fn(15))



