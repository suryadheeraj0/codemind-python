n=int(input())
s=0
s1=1
while(n>0):
    n1=n%10
    s=s+n1
    s1=s1*n1
    n=n//10
if(s==s1):
    print("Spy Number")
else:
    print("Not Spy Number")