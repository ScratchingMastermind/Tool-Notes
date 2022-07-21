'''
Create an application using Class for a school that displays the following info for students and Teachers:
Name(First and last)
School email
Pay - for the teachers
Exchange program info
'''


class Student:
    def __init__(self, first, last, major, gender, gpa, is_abroad):
        self.first = first
        self.last = last
        self.major = major
        self.gender = gender
        self.gpa = gpa
        self.is_abroad = is_abroad

    def exchange_program(self, country):
        if self.is_abroad is True:
            return "Currently in {}".format(country)
        else:
            return "Currently in Campus"


student1 = Student("Mastermind", "John", "Electronics", "Male", 3.7, False)
student2 = Student("Jin", "Fo", "Business", "Female", 3.7, True)

# print(student1.first)

# print(student1.exchange_program())
print(student2.exchange_program("Angola"))
