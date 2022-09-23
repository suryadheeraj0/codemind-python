def div(n):
    a=str(n)
    for j in a:
        if(int(j)==0 or n%int(j)!=0):
            return(0)
    else:
        return(1)
n1=int(input())
n2=int(input())
for i in range(n1,n2+1):
    if(div(i)):
        print(i,end=" ")