from classes.person import Person
import csv

class Student(Person):
    def __init__(self, name, age, role, school_id, password):
        super().__init__(name, age, role, password)
        self.school_id = school_id
        self.students = []
        
    def all_students(self):
        with open('data/students.csv') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for each_student in csv_reader:
                self.students.append(each_student)
        return self.students