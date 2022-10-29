import rps

class Person:
    def __init__(self, name, job):
        self.name = name
        self.job = job

    def talk(self):
        print("Hello I am " + self.name)

    def profession(self):
        print("I'm a " + self.job)
    
    def payment(self, hours, rate):
        print("My salary is $" + str(rps.salary(hours,rate)) + " per day")
        


class Engineer(Person):
    pass

class Doctor(Person):
    pass

eng1 = Engineer("Abhay","engineer")
eng1.talk()
eng1.profession()

doc1 = Doctor("Banner","doctor")
doc1.talk()
doc1.profession()
doc1.payment(10, 30)
