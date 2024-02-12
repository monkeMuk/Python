"""
Employees = name, age, rating

job = name,max employee( min rating 50), \, 
"""

class Employee:
    def __init__(self,name,age,rating):
        self.name = name
        self.age = age
        self.rating = rating

    def get_rating(self):
        return self.rating

class Job:
    def __init__(self,name,max_employee,min_rating):
        self.name = name
        self.max_employee = max_employee
        self.min_rating = min_rating

        self.employee_list = []
    
    def add_employee(self,Employee):
        if len(self.employee_list) < self.max_employee and Employee.rating > self.min_rating:
            self.employee_list.append(Employee)
            return True
        return False
         

e1 = Employee("A",23,56)
e2 = Employee("B",33,42)
e3 = Employee("C",65,12)

j1 = Job("D",2,20)

j1.add_employee(e1)
j1.add_employee(e2)
print(j1.add_employee(e3))

#   print(j1.employee_list[2].name)
