'''
Used when you want to create your own data type and organize your data.
In other words, to create a data type for an entity that exist on the real word. 
for example: DC motor, Student, Employee, etc.
'''

# define the class

'''
self.[attribute] = attribute -> is basically saying that the actually object attribute is the attribute that is being passed in.
And that attribute belongs to the object within that class
'''


class Student:
    def __init__(self, name, major, gender, gpa, is_abroad):
        self.name = name
        self.major = major
        self.gender = gender
        self.gpa = gpa
        self.is_abroad = is_abroad
        '''
        we can as well defined functions to do certain things.
        For example for the is_abroad attribute we would like to displayed some text 
        instead of True or false. Currently in [Country name]
        '''

        def exchange_program(self, country):
            if self.is_abroad is True:
                print("Currently in"+self.country)
            else:
                print("Currently in campus")
            return


# Now we can create an instance(object) of the student class.
student1 = Student("Mastermind", "Electronics", "Male", 3.7, False)
student2 = Student("Jin", "Business", "Female", 3.7, True)

# We can now access each of the attributes of the object
# print(student1.name)
# print(student2.name)

# setting the country name
student1exchange_program("Angola")
print(student1.is_abroad)
print(student1.is_abroad)
