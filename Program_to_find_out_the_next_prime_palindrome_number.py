n=int(input())
palin=[]
for i in range(n+1,n*50):
    t=i
    rev=0
    while i>0:
        n1=i%10
        rev=(rev*10)+n1
        i=i//10
    if t==rev:
        palin.append(t)
for j in palin:
    if j>1:
        for u in range(2,int(j**0.5)+1):
            if j%u==0:
                break
        else:
            print(j)
            break