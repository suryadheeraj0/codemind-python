n=input()
while(len(n)!=1):
    a=0
    for i in n:
        a=a+int(i)
    n=str(a)
print(n)