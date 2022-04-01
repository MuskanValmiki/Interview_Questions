class Person (object):
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname  = lastname  
    def name(self):
        print("FirstName :",self.firstname)
        print("LastName :",self.lastname)

class Student(Person):
    def __init__(self, firstname, lastname):
        super().__init__(firstname, lastname) 
    def show(self,class_type):
        role="Student"
        self.class_type = class_type
        print("Role :",role)

class Teacher(Person):
    def __init__(self, firstname, lastname):
        super().__init__(firstname, lastname)
        Mentor_name=input("Enter mentor name=")
    def teacher_class(self,subject):
        role = "Teacher"
        Mentor_name = ""
        self.subject = subject
        print("Role :",role)
        print("Mentor Name :",Mentor_name)
        print("Subject : ",subject)

name=input("enter your name: ")
last_name = input("enter your last name:")
humen = Person(name,last_name)
stu1= Student(name,last_name)
stu1.name()
stu1.show("Object")
teacher1 = Teacher(name,last_name)
teacher1.teacher_class("Python")
# here we are printing firstname and lastname and student information,teacher details.
