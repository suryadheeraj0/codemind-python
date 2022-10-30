n=int(input())
l=list(map(int,input().split()))
s=[]
s1=0
for i in range(len(l)):
    if l[i]%2!=0:
        s1=l[i]
print(s1)