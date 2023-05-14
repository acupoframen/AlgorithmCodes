import sys
input=sys.stdin.readline
dx=[1,-1,0,0,0,0]
dy=[0,0,-1,1,0,0]
dz=[0,0,0,0,1,-1]

while True:
    l,r,c=map(int,input().split())
    if (l,r,c)==(0,0,0):
        break
    data=[[]*r for _ in range(l)]
    dp=[[[0]*c for _ in range(r)] for _ in range(l)]
    visited=[[[0]*c for _ in range(r)] for _ in range(l)]
    for i in range(l):
        for j in range(r):
            data[i].append(list(map(str,input())))
        input()
    for i in range(l):
        for j in range(r):
            for k in range(c):
                if data[i][j][k]=="S":
                    sx,sy,sz=k,i,j
print(sx)