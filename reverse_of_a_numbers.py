n=int(input())
s=0
while(n>0):
    n1=n%10
    s=s*10+n1
    n=n//10
print(s)