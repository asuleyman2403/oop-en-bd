import copy

class SomeClass:
    def __init__(self, arr):
        self.array = arr

    
a = SomeClass([1, 2, 3])
# b = a
b = copy.copy(a) # equals to b = a
b.array[0] = 5
print(b.array)
print(a.array)

b = copy.deepcopy(a)
b.array[0] = 6
print(a.array)
print(b.array)






