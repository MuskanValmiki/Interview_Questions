N=int(input("enter any soldiers="))
i=1
even_count=0
odd_count=0
while i<=N:
    n=int(input("enter any number of weapens="))
    if n%2!=0:
        odd_count+=1
    else:
        even_count+=1
    i+=1
if even_count<odd_count:
    print("NOT READY")
elif even_count>odd_count:
    print("READY FOR BATTLE")
elif even_count==odd_count:
    print("NOT READY")
# mahasena question codechef



