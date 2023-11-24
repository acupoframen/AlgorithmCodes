n,m=map(int,input().split())
limit=[1e10]+list(map(int,input().split()))
inputs=[[] for _ in range(m+1)]
for i in range(1,n+1):
    data=list(map(int,input().split()))[:-1:]
    for j in data:
        inputs[j].append(i)
success=[[] for _ in range(n+1)]
for i in range(1,m+1):
    if len(inputs[i])>limit[i]:
        pass
    else:
        for j in inputs[i]:
            success[j].append(i)

for i in range(1,n+1):
    data=list(map(int,input().split()))[:-1:]
    for j in data:
        inputs[j].append(i)
for i in range(1,m+1):
    if len(inputs[i])>limit[i]:
        pass
    else:
        limit[i]-=len(inputs[i])
        for j in inputs[i]:
            success[j].append(i)

for i in range(1,n+1):
    if len(success[i]):
        print(*sorted(list(set(success[i]))))
    else:
        print("망했어요")