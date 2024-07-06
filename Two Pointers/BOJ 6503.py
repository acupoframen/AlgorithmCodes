from collections import deque
while True:
    m=int(input())
    if not m:
        break
    s=input()
    answer=0
    left=0
    right=0
    n=len(s)
    curr=[0 for _ in range(256)]
    while right<n:
        curr[ord(s[right])]+=1
        while curr.count(0)==256-m-1:
            curr[ord(s[left])]-=1
            left+=1
        answer=max(answer,right-left+1)
        right+=1

    print(answer)