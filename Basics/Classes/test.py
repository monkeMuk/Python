class Family:
    fam_num_count = 0
    age_increase = 2

    def __init__(self,title,name,age):
        self.title = title
        self.name = name
        self.age = age
        self.FullName = title + name

        Family.fam_num_count += 1

    def intro(self):
        print(f"{self.FullName} is {self.age} years old")

    def increase_age(self):
        self.age = int(self.age + self.age_increase)



F1 = Family("Uncle"," Jie",43,)
F2 = Family("Aunty"," Na",46)
F3 = Family("Uncle"," Long",54)

Family.intro(F1)
F2.intro()

F1.increase_age()
print(F1.age)

Family.intro(F1)

print(Family.fam_num_count)

