class BirthdayBoy:
    def __init__(self, name, age):
        self.name = name
        self.age= age
    def birthday(self):
        self.age=self.age+1
name=input("Enter your name=")
age=int(input("Enter your age="))
result= BirthdayBoy(name,age)
print(name,result.age,"old age")
result.birthday()
print(name,result.age,"new age")