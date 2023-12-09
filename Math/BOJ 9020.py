data=[0 for _ in range(10001)]
for i in range(2,101):
    if data[i]==0:
        for j in range(i*2,10001,i):
            data[j]=1

t=int(input())
for i in range(t):
    n=int(input())
    left=n//2
    right=n//2
    while True:
        if data[left]==0 and data[right]==0:
            print(left,right)
            break
        left-=1
        right+=1