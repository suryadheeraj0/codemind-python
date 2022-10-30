n=int(input())
l=list(map(int,input().split()))
z=int(input())
c=0
for i in range(len(l)):
    if l[i]==z:
        c+=1
    else:
        l[i]+1
print(c)