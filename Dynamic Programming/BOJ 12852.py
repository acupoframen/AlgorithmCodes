from collections import deque
n=int(input())
data=[0 for _ in range(n+1)]
q=deque([1])
if n==1:
    print(0)
    print(1)
    exit(0)
while q:
    k=q.popleft()
    if n==k+1 or n==2*k or n==3*k:
        data[n]=k
        break
    if 3*k<n and not data[3*k]:
        data[3*k]=k
        q.append(3*k)
    if 2*k<n and not data[2*k]:
        data[2*k]=k
        q.append(2*k)
    if not data[k+1]:
        q.append(k+1)
        data[k+1]=k

answer=[n]
val=n
while val!=1:
    val=data[val]
    answer.append(val)

print(len(answer)-1)
print(*answer)