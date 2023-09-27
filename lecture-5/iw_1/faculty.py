
class Faculty:
    def __init__(self, name, dean, room_number):
        self.name = name
        self.dean = dean
        self.room_number = room_number
        self.students = []

    def get_student_count(self):
        return len(self.students)

    def add_student(self, student):
        self.students.append(student)

    def withraw_student(self, student_id):
        students = []
        for student in self.students:
            if student.id != student_id:
                students.append(student)
        
        self.students = students



