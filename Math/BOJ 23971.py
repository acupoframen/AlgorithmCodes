from  math import ceil
h,w,n,m=map(int,input().split())
print(ceil(w/(m+1))*ceil(h/(n+1)))