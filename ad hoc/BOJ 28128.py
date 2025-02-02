import sys
input=sys.stdin.readline
n,m=map(int,input().split())
data=list(list(input().strip().split()) for _ in range(n))
answer=set()
for i in range(n):
    for j in range(m-2):
        if data[i][j]==data[i][j+2]:
            answer.add(data[i][j])
for i in range(n):
    for j in range(m-1):
        if data[i][j]==data[i][j+1]:
            answer.add(data[i][j])
for i in range(n-2):
    for j in range(m):
        if data[i][j]==data[i+2][j]:
            answer.add(data[i][j])
for i in range(n-1):
    for j in range(m):
        if data[i][j]==data[i+1][j]:
            answer.add(data[i][j])

answer=sorted(list(answer))
if not len(answer):
    print("MANIPULATED")
    exit(0)
for  i in answer:
    print(i)
