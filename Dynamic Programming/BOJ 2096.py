import sys
input=sys.stdin.readline
n=int(input())
dpmin=[[0 for _ in range(3)] for _ in range(n)]
dpmax=[[0 for _ in range(3)] for _ in range(n)]
dpmin[0]=list(map(int,input().split()))
dpmax[0]=dpmin[0]
for i in range(1,n):
    a,b,c=map(int,input().split())
    dpmax[i][0]=max(dpmax[i-1][0],dpmax[i-1][1])+a
    dpmax[i][1]=max(dpmax[i-1][0],dpmax[i-1][1],dpmax[i-1][2])+b
    dpmax[i][2]=max(dpmax[i-1][1],dpmax[i-1][2])+c
    dpmin[i][0]=min(dpmin[i-1][0],dpmin[i-1][1])+a
    dpmin[i][1]=min(dpmin[i-1][0],dpmin[i-1][1],dpmin[i-1][2])+b
    dpmin[i][2]=min(dpmin[i-1][1],dpmin[i-1][2])+c

print(max(dpmax[-1]), min(dpmin[-1]))