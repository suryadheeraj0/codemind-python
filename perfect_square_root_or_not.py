n=int(input())
t=0
f=0
for i in range(1,10):
    if i*i==n:
        t+=1
    else:
        f+=1
if(t>0):
    print("True")
else:
    print("False")