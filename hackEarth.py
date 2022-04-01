list=[]
n=len(list)
def bubble_sort(list,n):
    k=0
    while k<n-1:
        i=0
        while i<n-k-1:
            if list[i]>list[i+1]:
                temp=list[i]
                list[i]=list[i+1]
                list[i+1]=temp
            i+=1
        k+=1
    return list

def main():
    N=int(input("enter any place="))
    M=int(input("enter no of ants="))
    T=int(input("enter the time="))
    list.append(M)
    temp=M
    while temp:
        x=int(input("enter ="))
        y=int(input("enter any postion="))
        x=(N+x+((T*y))%N)
        i=0 
        while i<M:
            if x==0:
                x=N
            list.insert(i,x)
            i+=1
        temp-=1
    print(bubble_sort(list,n))
main()

