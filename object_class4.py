class Temprature():
    def  convertFahrenhiet(self,celsius):
        return (celsius*(9/5))+32
    def convertCelsius(self,farenhiet):
        return (farenhiet-32)*(5/9)
result=Temprature()
user=input("Enter in which you want to convert our temprature=")
if user=="Celsius":
    print(result.convertFahrenhiet(37))
elif user=="Fahrenhiet":
    print(result.convertCelsius(97))
else:
    print("you put temprature in kelvin and we did not made kelvin function")
    