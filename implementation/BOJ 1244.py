n=int(input())
data=[0]+list(map(int,input().split()))
k=int(input())
for _ in range(k):
    a,b=map(int,input().split())
    if a==1:
        for i in range(b,n+1,b):
            if data[i]:
                data[i]=0
            else:
                data[i]=1
    else:
        left=b-1
        right=b+1
        if data[b]:
            data[b]=0
        else:
            data[b]=1
        while True:
            if 1<=left and right<=n and data[left]==data[right]:
                if data[left]:
                    data[right]=data[left]=0
                else:
                    data[right]=data[left]=1
                left-=1
                right+=1
            else:
                break

data=data[1:]
for i in range(n//20+1):
    print(*data[i*20:(i+1)*20])