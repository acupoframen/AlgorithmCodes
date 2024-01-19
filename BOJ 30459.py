n,m,r=map(int,input().split())
loc=list(map(int,input().split()))
length=list(map(int,input().split()))

loc.sort()
length.sort()

answer=-1
left=0
right=n-1
