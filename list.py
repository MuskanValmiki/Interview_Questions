list=['A','B']
num=int(input("enter any number="))
i=1
while i<=num:
    index=0
    while index<len(list):
        print(list[index]+str(i))
        index+=1
    i+=1
    