class Student():
    def __init__(self,name,roll):
        self.name = name
        self.roll= roll
    def display(self):
        print(self.name)
        print(self.roll)
    def setAge(self,age):
        self.age=age
        return self.age
    def setMarks(self,marks):
        self.marks = marks
        return self.marks
name=input("Enter your name=")
setAge=int(input("Enter your age="))
setMarks=int(input("Enter your marks="))
result=Student(name,setAge)
user=input("Enter what you want to do display\nsetAge\nsetMarks=")
if user=="display":
    result.display()
elif user=="setAge":
    print(result.setAge(setAge))
elif user=="setMarks":
    print(result.setMarks(setMarks))
else:
    print("you choice options out of option")