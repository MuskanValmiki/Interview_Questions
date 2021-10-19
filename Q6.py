num=int(input("enter how many customer are in line"))
i=1
time_list=[]
while i<=num:
    order,preparation=input("enter your order and preparation time=").split()
    time=int(order)+int(preparation)
    time_list.append(time)
    i+=1
index=0
count=0
while index<len(time_list):
    if time_list[index] in time_list:
        count+=1
        if count>1:
            j=0
            while j<len(time_list):
                k=0
                while k<len(time_list):
                    if time_list[j]<time_list[k]:
                        time_list[j],time_list[k]=time_list[k],time_list[j]
                    k+=1
                j+=1
            a=time_list
    else:
        a=time_list
    index+=1
print(a)
# jim anti order hackerrank question 