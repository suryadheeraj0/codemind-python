n=int(input())
sum=0
e=n*n
while(e>0):
    d=e%10
    sum=sum+d
    e=e//10
if(sum==n):
    print("Neon Number")
else:
    print("Not Neon Number")