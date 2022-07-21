# Class Inheritance allows us to inherit attributes and methods from the parent class.
# We get the functionality of the parent class, as well you can override or add new function without affecting the parent class

'''assume that we have to create a different of employee. Ex: Dev. or managers. You can just inherit the functions and add new ones.
'''


class Employee():
    raise_amount = 1.04  # class variable for the raise amount
    num_of_emp = 0  # numbers of employees

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'

        Employee.num_of_emp += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

# Inherit from the Employee Class


class Developer(Employee):
    # it overrides the original raise amount from 4 to 10%
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        # First, last, pay, are going to be handle by the Employee Class
        # prog_lang is going to be handle by Developer Class
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

# Inherit from the Employee Class


class Managers(Employee):
    # Here you're going to pass a list of employees that each manager supervises.
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    # the ability to add ,remove and printout employee from list
    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def rm_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employees(self):
        for emp in self.employees:
            print("--->", emp.fullname())


dev_1 = Developer("Gin", "Ford", 600, "Python")
dev_2 = Developer("Tom", "Mike", 500, "C")

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

# print(dev_1.email)  # from Employee class
# print(dev_1.prog_lang)  # from Developer class

# Using the Managers class

mgr_1 = Managers("Sue", "Yo", 800, [dev_1])
mgr_1.add_employee(dev_2)
print(mgr_1.email)
mgr_1.print_employees()
print("rm Function")
mgr_1.rm_employee(dev_1)
mgr_1.print_employees()

# checking whether mgr_1 is an instance of Manager
print(isinstance(mgr_1, Managers))
# checking whether Manager is a subclass of Developer
print(issubclass(Managers, Developer))
