from itertools import permutations
n=int(input())
data=list(map(int,input().split()))
answer=0
for temp in permutations(data,n):

    val=0
    for j in range(n-1):
        val+=abs(temp[j+1]-temp[j])

    answer=max(answer,val)
print(answer)