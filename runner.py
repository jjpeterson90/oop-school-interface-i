from classes.school import School
from classes.student import Student
from classes.staff import Staff
from classes.person import Person

school = School('Ridgemont High')

student_info = {'name': 'Diana', 'password': 'password', 'school_id': 12345, 'age': 17, 'role':'Student'}

Student(**student_info)

print(school.name)
print(school.staff)
print(school.students)