n=int(input())
l=list(map(int,input().split()))
s=[]
s1=[]
for i in range(len(l)):
    if l[i]%2==0:
        s.append(l[i])
    else:
        s1.append(l[i])
for x in s1:
    s.append(x)
for j in s:
    print(j,end=' ')