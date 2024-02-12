class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade
    
    def new_grade(self,grade):
        self.grade = grade

class Course:
    def __init__(self,name,max_stu,min_age):
        self.name = name
        self.max_stu = max_stu
        self.min_age = min_age
        self.students = []

    def add_students(self,student):
        if len(self.students)< self.max_stu and student.age < self.min_age:
            self.students.append(student)
            return True
        return False

    def show_students(self):
        return self.students

    def get_average(self):
        value = 0
        for student in self.students:
            value += student.get_grade()    # can also be grade

            return int(value/len(self.students))

 

             
#a = Student("nick",34,54)
#print(a.new_grade(23))
#print(a.get_grade())
s1 = Student("Adam",12,24)
s2 = Student("Bob",13,44)
s3 = Student("Charlie",16,75)


c1 = Course("Maths",2,40)
c1.add_students(s1)
c1.add_students(s2)
c1.add_students(s3)

print(c1.students[2].name)
#print(c1.get_average())
