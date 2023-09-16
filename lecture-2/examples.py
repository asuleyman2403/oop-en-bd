
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

class Student(Person):
    students_count = 0

    def __init__(self, name, age):
        Student.students_count += 1
        Person.__init__(self, name, age)

    def __del__(self):
        Student.students_count -= 1    

assyl = Student("Assyl", 23)
alibek = Student("Alibek", 22)
print(Student.students_count)
del alibek
print(Student.students_count)
