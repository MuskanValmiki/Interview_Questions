class ExampleClass :
    def func(self,name,age):
        self.name=name
        self.age=age
        return (self.name,self.age)
name=input("Enter your name=")
age=int(input("Enter your age="))
result= ExampleClass()
print(result.func(name,age))