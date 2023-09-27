

class Student:
    # class attributes (static fields)
    student_count = 0

    # object attributes (non static fields / objects fields)
    # full_name = 'Assyl Suleiman'
    # id = 123
    # s_course = 1
    # s_faculty = 'SDS'
    # speciality = 'SE'
    # is_local_student = False
    # subjects = ['OOP']
    # semester = 1

    # access modifiers: private, protected, public
    # __full_name = 'Assyl Suleiman' private
    # _full_name = 'Assyl Suleiman' protected
    # full_name = 'Assyl Suleiman' public

    def __init__(self, name, surname, student_id, course, faculty, speciality):
        Student.student_count = Student.student_count + 1
        self.full_name = name + ' ' + surname
        self.id = student_id
        self.s_course = course
        self.s_faculty = faculty
        self.speciality = speciality
        self.subjects = []
        self.semester = 1

    def __del__(self):
        Student.student_count -= 1

    def get_all_info(self):
        print(self.full_name, self.id, self.s_course, self.semester, self.s_faculty, self.speciality)
        print(f"Subjects: {', '.join(self.subjects)}")
        # OOP, web dev, backend
    
    # getter
    def get_full_name(self):
        return self.full_name

    # setter
    def set_full_name(self, full_name):
        self.full_name = full_name

    def add_subject(self, subject):
        self.subjects.append(subject)

    def transfer_to_next_semestr(self):
        self.semester = self.semester % 2 + 1
        self.s_course = self.s_course + (1 if self.semester == 1 else 0)

if __name__ == '__main__':
    print('CHECK CHECK')


# Something like
# self = {
#     'full_name': 'Assyl Suleiman',
#     'speaciality': 'SE'
# }

# PUBLIC
# assyl = Student("Assyl", "Suleiman")
# assyl.full_name = 'Assyl'
# print(assyl.full_name)

# PROTECTED
# assyl = Student('name', 'surname')
# print(assyl._full_name) CAN NOT
# assyl._full_name = 'Assyl' CAN NOT
# inside of class
# class Subclass(Student):
#     def method(self, full_name):
#         self._full_name = full_name

# PRIVATE __full_name
# only inside of class (Student)

    