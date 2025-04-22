n,k=map(int,input().split())
data=list(map(int,input().split()))
ryan=list()
for i in range(n):
    if data[i] == 1:
        ryan.append(i)
if len(ryan) <k:
    print(-1)
    exit(0)
answer=1e10
for i in range(len(ryan)-k+1):
    answer=min(answer,ryan[i+k-1]-ryan[i]+1)
print(answer)