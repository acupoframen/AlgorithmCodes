import sys
import bisect
input=sys.stdin.readline
def binarysearch(i, j, k):
    lo, hi =1,2**31
    while lo <= hi:
        mid = (lo + hi) // 2
        cnt = bisect.bisect_right(a, mid, 0, i) + bisect.bisect_right(b, mid, 0, j)
        if cnt >= k:
            ans = mid
            hi = mid - 1
        else:
            lo = mid + 1
    idx = bisect.bisect_left(a, ans, 0, i)
    if idx < i and a[idx] == ans:
        return 1, idx + 1  
    else:
        idx = bisect.bisect_left(b, ans, 0, j)
        return 2, idx + 1  

n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
q=int(input())
for _ in range(q):
    i,j,k=map(int,input().split())
    print(*binarysearch(i,j,k))