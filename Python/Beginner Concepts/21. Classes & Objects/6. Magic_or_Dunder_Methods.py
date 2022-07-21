class Employee():
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # These special functions are called Dunder(the double underscore)
    # They are a set
    # Unambiguous representation of the object - used to for loggging, debuging
    def __repr__(self):
        return "Employee('{}','{}','{}')".format(self.first, self.last, self.pay)
    # A more readable representation of the object - used as display for the end user

    def __str__(self):
        return "{} - {}".format(self.fullname(), self.email)

    # For the sake of showcase, how you would add two pays from different employees.
    def __add__(self, other):
        return self.pay + other.pay
    # Find out the number of character a name as

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee('Carlos', "Jim", 100)
emp_2 = Employee("Test", "User", 200)
'''
print(emp_1)
This prints:
<__main__.Employee object at 0x7ff2657d3c10> 
if you would be nice if we can change to something more unfriendly
'''

# After Dunder __rep__ only.

'''
print(emp_1)
This prints:
Employee('Carlos','Jim','100')
'''
# After Dunder __rep__ and __str__. It takes the __str__ first.
print(emp_1)

'''
print(emp_1)
This prints:
Carlos Jim - Carlos.Jim@email.com
'''

# You can also print both
# print(str(emp_1))
# print(repr(emp_1))

# Using dunder add

print(emp_1 + emp_2)

# Using dunder length

print(len(emp_1))
