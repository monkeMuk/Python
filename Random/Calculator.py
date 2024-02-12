class Calculator:
    def __init__(self,num1,num2):
        self.number1 = num1
        self.number2 = num2 
    
    def add(self):
        return self.number1 + self.number2 
    def minus(self):
        return self.number1 - self.number2 
    def times(self):
        return int(self.number1 * self.number2)
    def divide(self):
        return int(self.number1 / self.number2)

    def decision(self,user_decision):
        if user_decision == "-":
            return self.minus()
        elif user_decision == "+":
            return self.add()
        elif user_decision == "*":
            return self.times()
        elif user_decision == "/":
            return self.divide()


#calc = Calculator(4,3)
    #int(input("Insert num1:     ")),
    #int(input("Insert num2:     ")),
    #)
#print(calc. ("-"))

user = input("insert num")
user = user.split("")
print(user)