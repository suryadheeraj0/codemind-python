x,y=map(int,input().split())
if x>y:
    gr=x
else:
    gr=y
while(True):
    if((gr%x==0) and (gr%y==0)):
        lc=gr
        break
    gr+=1
print(lc)