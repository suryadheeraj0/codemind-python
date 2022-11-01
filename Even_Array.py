n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in range(len(l)):
    if l[i]%2==0:
        l1.append(True)
    else:
        l1.append(False)
if False in l1:
    print("False")
else:
    print("True")
