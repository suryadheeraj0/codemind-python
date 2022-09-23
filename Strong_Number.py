n=int(input())
t=n
c=0
while(n>0):
    n1=n%10
    s=1
    for i in range(1,n1+1):
        s=s*i
    c+=s
    n=n//10
if(c==t):
    print("The number %d is a strong number"%t)
else:
    print("The number %d is not a strong number"%t)