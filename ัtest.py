#create class
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}") 
# create object
emp1 = Employee("John Doe", 30, 50000)
emp2 = Employee("Jane Smith", 25, 60000)
# call method
emp1.display()
emp2.display()  
emp3 = Employee("Alice Johnson", 28, 55000)
emp3.display()
    