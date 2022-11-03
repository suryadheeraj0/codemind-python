n=int(input())
n1=int(input())
n2=n+n1
p=[]
for i in range(n2*2):
    if i>1:
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                break
        else:
            p.append(i)
for k in range(1,n2*2):
    if(n2+k) in p:
        print(k)
        break