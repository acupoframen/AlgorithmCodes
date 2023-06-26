import sys
input=sys.stdin.readline
tc=int(input())
for _ in range(tc):
    n,m,w=map(int,input().split())
    data=[]
    for _ in range(m):
        s,e,t=map(int,input().split())
        data.append([s,e,t])
        data.append([e,s,t])
    for _ in range(w):
        s,e,t=map(int,input().split())
        data.append([s,e,-t])
    noFlag=0
    
    distance=[1e10]*(n+1)
    distance[1]=0
    for i in range(1,n):
        for j in range(len(data)):
            curr=data[j][0]
            next=data[j][1]
            val=data[j][2]
            if  distance[next]>distance[curr]+val:
                distance[next]=distance[curr]+val
                if i==n-1:
                    noFlag=1
                    break
            if noFlag:
                break
        if noFlag:
            break
    if noFlag:
        print("YES")
    else:
        print("NO")