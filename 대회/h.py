import sys
sys.setrecursionlimit(int(5*1e5+1))
input=sys.stdin.readline
n=int(input())

names=[0]+list(input().strip() for _ in range(n))
data=[list() for _ in range(n+1)]
answer=[]
def dfs(num):
    answer.append(num)
    for i in data[num]:
        dfs(i)
        return
first=0
for i in range(n-1):
    a,b=map(int,input().split())
    data[a].append(b)
    if i==n-2:
        first=a
realanswer=""
dfs(first)
for i in range(n):
    realanswer+=names[answer[i]]
print(realanswer) 