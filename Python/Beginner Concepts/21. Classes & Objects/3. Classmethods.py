'''
Regular methods in a class automatically take the instance as the first argument. In this case "self"
Class methods take the class as the first argument. To do that we use decorators: @classmethod
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

    @classmethod
    # cls is the variable name instead of self
    def set_raise_amount(cls, amount):
        # changing the the global raise amount
        cls.raise_amount = amount

    @classmethod
    def add_employee(cls, emp_info):
        first, last, pay = emp_info.split("-")
        return cls(first, last, pay)


emp_1 = Employee('Carlos', "Jim", 100)
emp_2 = Employee("Test", "User", 200)

'''
# since the first instance is the class, we just need to pass the amount.
# This same as Employee.raise_amount = 1.05, But now we use a class method.

# Employee.set_raise_amount(1.05)
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

Class methods can also be used as alternative constructors.
You use this class methods in order to provide multiple ways to create an object/instances
For example, you have the following data:
emp_3  = 'John-Mclovin-500'
emp_4 = 'Thor-Odinson-400'
Instead of parsing the string before creating an employee, how about you pass the whole string?
'''
# The manual way

# emp_3 = 'John-Mclovin-500'
# emp_4 = 'Thor-Odinson-400'

# first, last, pay = emp_3.split("-")
# new_emp_3 = Employee(first, last, pay)
# new_emp_4 = Employee(first, last, pay)

# print(new_emp_3.email)
# print(Employee.num_of_emp)

# The smart way

emp_3 = 'John-Mclovin-500'
emp_4 = 'Thor-Odinson-400'
new_emp3 = Employee.add_employee(emp_3)
new_emp4 = Employee.add_employee(emp_4)

print(new_emp3.email)
print(Employee.num_of_emp)
