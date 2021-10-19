def fun(i):
    if i==10:
        return i
    print(i)
    return fun(i+1)
print(fun(1))
# one to ten print 

def table(i):
    if i==10:
        return 
    print(num,"*",i,"=",num*i)
    return table(i+1)
num=int(input("enter any number="))
print(table(1))
# table
