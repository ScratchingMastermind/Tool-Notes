# gives a "special" functionality to methods within a class as:
# Getters, Setters, or Deleters when we define properties in a class
# Also you get to call it as an attribute rather than a function

class Employee():

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    # Getters - Gets the property in a specific format in case email.
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # Sets a given input to a stander output
    # In this case splits the given name string.
    # Using fullname as a format.
    @fullname.setter
    def fullname(self, name):
        first, last = name.split("-")
        self.first = first
        self.last = last

    # deletes a certain entry.
    @fullname.deleter
    def fullname(self):
        print("Deleted Name")
        self.first = None
        self.last = None


emp_1 = Employee('Carlos', "Jim", 100)

# changing emp_1 first name, because of the decorator it will update everything
emp_1.first = 'Jim'
# Without using @fullname.setter this function won't work.
emp_1.fullname = "River-Nile"
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

# deletes emp_1
del emp_1.fullname
