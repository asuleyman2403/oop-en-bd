class Employee:
    def __init__(self, name, salary, rank):
        self.name = name
        self.salary = salary
        self.rank = rank

    def __add__(self, other):
        salary = emp_one.salary + emp_two.salary
        rank = 0
        if emp_one.rank < emp_two.rank:
            rank = emp_two.rank
        else:
            rank = emp_one.rank
        employee = Employee(None, salary, rank)

        return employee

    def __eq__(self, other):
        return self.rank == other.rank and self.salary == other.salary

    def __lt__(self, other):
        print(self.rank, other.rank)
        if self.rank < other.rank:
            return True
        else:
            if self.rank == self.rank:
                return self.salary < other.salary
            else:
                return False

    def __reps__(self):
        pass
    
    def __str__(self):
        return self.name

    def __del__(self):
        pass


emp_one = Employee("Alua", 80000, 1)
emp_two = Employee("Aldina", 100000, 2)

emp_third = emp_one + emp_two
emp_third.name = "Andrey"

# if emp_one == emp_two:
#     print("They are equal")
# else:
#     print("The are not equal")

# print(emp_third.salary)
# print(emp_third.rank)

# print(emp_one < emp_two)


print(str(emp_one))

del emp_one

