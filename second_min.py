n=[50,49,23,56,100,98]
max=n[0]
min=n[0]
sec_max=None
sec_min=None
index=0
while index<len(n):
    if n[index]>max:
        sec_max=max
        max=n[index]
    elif sec_max == None or sec_max<n[index]:
        sec_max=n[index]
    if n[index]<min:
        sec_min=min
        min=n[index]
    elif sec_min == None or sec_min>n[index]:
        sec_min=n[index]
    index+=1
print(sec_min,"second min")