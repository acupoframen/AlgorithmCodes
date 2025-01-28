from collections import deque
n=int(input())
team1=[]
team2=[]
ban=[0]
q=deque()
for i in range(n):
    ban.append(list(map(int,input().split()))[1:])
    q.append(i+1)
def dfs(person,isteam1):
    if isteam1:
        team1.append(person)
    else:
        team2.append(person)
    for i in ban[person]:
        if i in q:
            q.remove(i)
            dfs(i, not isteam1)

while q:
    i=q.popleft()
    dfs(i,1)
team1.sort()
team2.sort()
print(len(team1))
print(*team1)
print(len(team2))
print(*team2)