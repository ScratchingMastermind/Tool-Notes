'''
Used to logically group our data and function in way that's easy to reuse and also build upon.
Method = a function that is associated with a class.
Attribute = characteristics of the class

In other words, when you want to create your own data type and organize your data.
in order to create a data type for an entity that exist on the real word. 
for example: DC motor, Student, Employee....you can use a class.
'''
# Consider having to make an application for a company and u have to represent the different type of employees.
# Here each employee will have difference attributes and methods. for example pay, email, name etc.


class Employee():

    # the attributes of the class -> Instance Variables - which will be unique to every instance of the class
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'

    # Methods - the ability to perform some kind of action
    # For example: The ability to display fullname of an employee
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


# Instances of the Employee class - we use the employee class as a blueprinting
emp_1 = Employee('Carlos', "Jim", 200)
emp_2 = Employee("Test", "User", 200)
# Prints email
print(emp_1.email)
print(emp_2.email)
# prints full name - notice the () indicates that this is a Method not and an attribute.
print(emp_1.fullname())
print(emp_2.fullname())
# Same can be achieve by using the Class
print(Employee.fullname(emp_1))
print(Employee.fullname(emp_2))
