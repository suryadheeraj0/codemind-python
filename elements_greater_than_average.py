n=int(input())
l=list(map(int,input().split()))
s=0
c=0
for i in range(len(l)):
    s+=l[i]
    s1=s//n
for j in range(len(l)):
    if(l[j]>=s1):
        c+=1
print(c)
        
        