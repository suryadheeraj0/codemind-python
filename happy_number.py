n=input()
while(len(n)!=1):
    a=0
    for i in n:
        a=a+int(i)**2
        n=str(a)
if a==1 or a==7:
    print("True")
else:
    print("False")