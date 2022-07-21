'''
Class variables - variables that are shared among all instances of class.
Unlike Instance variables which are unique to each instance.
'''


class Employee():
    raise_amount = 1.04  # class variable for the raise amount
    num_of_emp = 0  # numbers of employees

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'

        # here it makes no sense to make unique number of employee as we want the total.Thus self.num_of_emp is not used.
        # As this runs every time an instance is created, we can increment the variable here.
        Employee.num_of_emp += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # a function that will apply a raise to all instances of the class
    # This apply 4% to the current pay.
    def apply_raise(self):
        # Variable raise_amount here needs to be accessed through the class itself(Employee.raise_amount) or as an instance of the class
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee('Carlos', "Jim", 100)
emp_2 = Employee("Test", "User", 200)

'''
It accesses the rise_amount from the Employees class and changes to 5%
Employee.raise_amount = 1.05
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
'''
# It changes the raise amount to one employee only to 7%
# It doesn't override the global 4%
emp_1.raise_amount = 1.07
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# printing number of employee
print(Employee.num_of_emp)
