n=int(input())
data=[list(map(int,input().split())) for _ in range(n)]
data.sort(key=lambda x: (-x[0],x[1]))
answer=0
for i in range(5,n):
    if data[i][0]==data[4][0]:
        answer+=1
    else:
        break
print(answer)