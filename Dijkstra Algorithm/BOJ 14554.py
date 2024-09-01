import heapq
import sys
input=sys.stdin.readline
n,m,s,e=map(int,input().split())
mod=int(1e9)+9
adj=list([] for _ in range(int(1e5)+1))
for _ in range(m):
    a,b,c=map(int,input().split())
    adj[a].append([b,c])
    adj[b].append([a,c])
dist=list(1e20 for _ in range(int(1e5)+1))
dp=list(0 for _ in range(int(1e5)+1))
q=[]
dist[s]=0
heapq.heappush(q,[0,s])
dp[s]=1
while q:
    currdist,curr=heapq.heappop(q)
    if dist[curr]!=currdist:
        continue
    for next, nextdist in adj[curr]:
        if dist[next] < currdist+nextdist:
            continue
        elif dist[next] == currdist+nextdist:
            dp[next]=(dp[next]+dp[curr])%mod
        else:
            dist[next]=(currdist+nextdist)
            heapq.heappush(q,[dist[next],next])
            dp[next]=dp[curr]
print(dp[e]%mod)