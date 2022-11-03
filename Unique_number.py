n=input()
a=set(n)
l=[]
b=list(a)
for i in n:
    l.append(i)
if(len(b)==len(l)):
    print("Unique Number")
else:
    print("Not Unique Number")