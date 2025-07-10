n=int(input())
answer=1e10
for _ in range(n):
    data=list(map(int, input().split()))
    if sum(data)>=512:
        answer=min(answer,sum(data))
if answer==1e10:
    print(-1)
else:
    print(answer)