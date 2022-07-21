'''
static methods - don't pass anything automatically unlike regular methods(self) and class methods(cls).
Thus, they behave just like regular functions but they have some logical connection with the class.
when to use class method and static method?
if you don't access the instances or the class within the function then function should be static.
'''
import datetime


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
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def add_employee(cls, emp_info):
        first, last, pay = emp_info.split("-")
        return cls(first, last, pay)

    @staticmethod
    def is_Workday(day):
        # does the day fall in weekday.
        # 5=>saturday,6=> Sunday.
        if day.weekday() == 5 or day.weekday() == 6:
            return print("Weekend")
        else:
            return print("Weekday")


emp_1 = Employee('Carlos', "Jim", 100)
emp_2 = Employee("Test", "User", 200)

'''
Assume that we need a simple function that returns whether or not that was a work day.
it has some logical connection with the class Employee but not with instances or variables of this class
'''
my_date = datetime.date(2022, 7, 20)

Employee.is_Workday(my_date)
