from classes.person import Person
import csv

class Staff(Person):
    def __init__ (self, name, age, role, employee_id, password):
        super().__init__(name, age, role, password)
        self.employee_id = employee_id
        self.staff = []
        
    def all_staff(self):
        with open('data/staff.csv') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for each_staff in csv_reader:
                self.staff.append(each_staff)
        return self.staff