n=int(input())
s1=[]
s2=[]
while(n>0):
    n1=n%10
    if(n1%2==0):
        s1.append(n1)
    else:
        s2.append(n1)
    n=n//10
if(len(s1)>=1) and (len(s2)>=1):
    print("Mixed")
elif(len(s1)>=1) and (len(s2)==0):
    print("Even")
else:
    print("Odd")

    