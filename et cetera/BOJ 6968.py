import sys
sys=sys.stdin.readline
n,k=map(int,input().split())
data=[float(input()) for _ in range(n)]
data.sort()
jeol=(sum(data[k:n-k]))/(n-2*k)
print("%.2f" %(jeol+1e-8))
bo=(sum(data[k:n-k])+data[k]*k+data[n-k-1]*k)/n
print("%.2f" %(bo+1e-8))
