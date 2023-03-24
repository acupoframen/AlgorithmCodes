n=int(input())
data=list(map(int,input().split()))
somo=0
last=1e10
stack=2
for i in range(n):
    if last==1e10:
        somo=2
    elif last==data[i]:
        somo+=stack
    else:
        somo+=2
        stack=2
    last=data[i]
    stack*=2
    if somo>=100:
        somo=0
        stack=2
        last=1e10
print(somo)