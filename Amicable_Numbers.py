n=int(input())
n1=int(input())
s=0
s1=0
for i in range(1,n):
    if n%i==0:
        s=s+i
for j in range(1,n1):
    if n1%j==0:
        s1=s1+j
if(n1==s) and (n==s1):
    print("Amicable")
else:
    print("Not Amicable")
        