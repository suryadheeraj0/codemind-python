n=int(input())
l=list(map(int,input().split()))
s=0
for i in range(len(l)):
    s=s+l[i]
    s1=s//len(l)
if s1 not in l:
    print("False")
else:
    print("True")
    