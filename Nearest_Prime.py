n=int(input())
for i in range(n):
    a=int(input())
    a1=a
    while True:
        is_Prime=True
        for i in range(2,int(a1**0.5)+1):
            if(a1%i==0):
                is_Prime=False
                break
        if is_Prime==True:
            break
        else:
            a1+=1
    a2=a
    while True:
        is_Prime=True
        for i in range(2,int(a2**0.5)+1):
            if(a2%i==0):
                is_Prime=False
                break
        if is_Prime==True:
            break
        else:
            a2-=1
    if a1-a>a-a2:
        print(a2)
    elif a1-a==a-a2:
        print(a2)
    else:
        print(a1)
    