'''
Create an application using Class for a school that displays the following info for students and Teachers:
> Students
Name(First and last)
School email
Exchange program info - are they abroad if so where?

> Teachers
Same as students with additional information like
Pay - for the teachers
numbers of students in their class
'''


class Teachers:
    def __init__(self, first, last, pay=None, students=None):
        self.first = first
        self.last = last
        self.pay = pay

        if students is None:
            self.students = []
        else:
            self.students = students

    @property
    def fullname(self):
        return "> {} {}".format(self.first, self.last)

    @property
    def email(self):
        return "{}.{}@school.com".format(self.first, self.last)

    def student_display(self):
        for std in self.students:
            print(std.fullname)


class Student(Teachers):

    def __init__(self, first, last, major, gender, gpa, is_abroad):
        super().__init__(first, last)
        self.major = major
        self.gender = gender
        self.gpa = gpa
        self.is_abroad = is_abroad

    def exchange_program(self, country=None):
        if self.is_abroad is True:
            return "Currently in {}".format(country)
        else:
            return "Currently in Campus"


# Instances of students
student1 = Student("Mastermind", "John", "Electronics", "Male", 3.7, True)
student2 = Student("Jin", "Fo", "Business", "Female", 4, False)
student3 = Student("Tom", "Ye", "Mechanical", "Female", 3.2, False)
student4 = Student("Gab", "Tan", "Electronics", "Female", 3, True)

# Instances of Teachers
teach1 = Teachers("John", "Tim", 1000, [student1, student2])
teach2 = Teachers("Kate", "Tim", 1000, [student4, student3])


print("\n---> Student Info")
print("{} --> {} --> {}".format(student1.fullname,
      student1.email, student1.exchange_program("Angola")))
print("{} --> {} --> {}".format(student2.fullname,
      student1.email, student2.exchange_program()))
print("{} --> {} --> {}".format(student3.fullname,
      student3.email, student3.exchange_program()))
print("{} --> {} --> {}".format(student4.fullname,
      student1.email, student4.exchange_program("Canada")))

print("\n---> Teacher 1 Info")
print("{} --> {} --> ${}".format(teach1.fullname,
      teach1.email, teach1.pay))
print("---> N of Students")
teach1.student_display()

print("\n---> Teacher 2 Info")
print("{} --> {} --> ${}".format(teach2.fullname,
      teach2.email, teach2.pay))
print("---> N of Students in the class")
teach2.student_display()
