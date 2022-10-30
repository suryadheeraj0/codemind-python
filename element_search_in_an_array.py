n=int(input())
l=list(map(int,input().split()))
a=int(input())
for i in range(len(l)):
    if l[i]==a:
        print('True')
        break
    else:
        l[i]+1
if a not in l:
    print("False")