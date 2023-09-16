class Faculty:
    def __init__(self, name):
        self.name = name
        self.students_count = 0

    def get_students_count(self):
        return self.students_count

    def increment_student_count(self):
        self.students_count += 1
        
    
class Student:
    def __init__(self, name, surname, faculty):
        self.name = name
        self.surname = surname
        self.faculty = faculty
        faculty.increment_student_count()


sds = Faculty("School of Digital Sciences")
sbm = Faculty("School of business and management")

andrey = Student("Andrey", "Tsay", sds)
zhamilya = Student("Zhamilya", "Akhan", sds)

alua = Student("Alua", "Duysekova", sbm)

print(sds.get_students_count())
print(sbm.get_students_count())


