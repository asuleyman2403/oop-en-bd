from student import Student
from faculty import Faculty


assyl = Student('Assyl', 'Suleiman', 123, 1, 'SDS', 'SE')
alua = Student('Alua', 'Duysekova', 456, 3, 'SDS', 'BD')

# print('#######')
# alua.get_all_info()
# print('#######')
# alua.transfer_to_next_semestr()
# alua.transfer_to_next_semestr()
# print('#######')
# alua.get_all_info()
# alua.add_subject('OOP')
# alua.add_subject('Backend')
# alua.get_all_info()

# print(Student.student_count)
# del assyl
# print(Student.student_count)

sds = Faculty('School of Digital Science', 'Kyanush Abeshev', 315)
sds.add_student(assyl)
sds.add_student(alua)
print(sds.get_student_count())
sds.withraw_student(assyl.id)
print(sds.get_student_count())

