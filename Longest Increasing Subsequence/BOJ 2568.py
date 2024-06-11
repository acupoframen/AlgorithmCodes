n=int(input())
data=list(list(map(int,input().split())) for _ in range(n))
data.sort()
lis=[data[0]]
indexlist=[0]
count=1
parents=[i for i in range(n+1)]
def binary_search(i):
    left=0
    right=len(lis)-1
    while left<=right:
        mid=(left+right)//2
        if lis[mid][1]<i:
            left=mid+1
        else:
            right=mid-1
    return left
for i in range(1,n):
    if lis[-1][1]<data[i][1]:
        lis.append(data[i])
        indexlist.append(count)
        count+=1
    else:
        index=binary_search(data[i][1])
        lis[index]=data[i]
        indexlist.append(index)
print(n-count)
conn=set()
findidx=count-1
for idx, insertedidx in enumerate(indexlist[::-1]):
    if findidx==insertedidx:
        conn.add(n-idx-1)
        findidx-=1
    if findidx<0:
        break
for i in range(n):
    if i not in conn:
        print(data[i][0])