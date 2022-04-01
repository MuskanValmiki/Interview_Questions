# find the factorial by using for loop and if else conditions.
num=int(input("enter any number="))
factorial = 1
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
print("The factorial of",num,"is",factorial)



# find the factorial bu using while loop.
factorial=1
num=int(input("enter any number="))
i=1
while i<=num:
  factorial=factorial*i
  i+=1
print(factorial)