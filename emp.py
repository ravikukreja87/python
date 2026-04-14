class Person(object):
    def __init__ (self,name,idnumber):
        self.name = name
        self.idnumber = idnumber
    def display(self):
        print("Name:", self.name)
        print("ID Number:", self.idnumber)
class Employee(Person):
    def __init__ (self,name , idnumber, photo, salary):
        self.photo=photo
        self.salary=salary
        Person.__init__(self,name, idnumber)
f=Employee("Samarth", 1234576890987554, "samarth.jpg", 5000000)

f.display()
print("Photo:", f.photo)
print("Salary:", f.salary)