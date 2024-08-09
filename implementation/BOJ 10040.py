n,m=map(int,input().split())
data=list(int(input()) for _ in range(n))
st=list(int(input()) for _ in range(m))
answer=list(0 for _ in range(n))
for i in range(m):
    for j in range(n):
        if data[j]<=st[i]:
            answer[j]+=1
            break
print(answer.index(max(answer))+1)