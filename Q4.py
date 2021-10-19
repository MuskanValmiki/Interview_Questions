N=int(input("enter any soldiers="))
a=[]
i=1
while i<=N:
    n=int(input("enter any number of weapens="))
    a.append(n)
    i+=1
index=0
even_count=0
odd_count=0
while index<len(a):
    if a[index]%2!=0:
        odd_count+=1
    else:
        even_count+=1
    index+=1
if even_count<odd_count:
    print("NOT READY")
elif even_count>odd_count:
    print("READY FOR BATTLE")
elif even_count==odd_count:
    print("NOT READY")
# mahasena question codechef



