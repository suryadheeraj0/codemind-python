n=int(input())
t=n*n
r=0
while(n>0):
    n1=n%10
    r=r*10+n1
    n=n//10
r1=r*r
r3=0
while(r1>0):
    r2=r1%10
    r3=r3*10+r2
    r1=r1//10
if(r3==t):
    print("True")
else:
    print("False")
    