from itertools import permutations
from collections import deque
import copy
n=int(input())
data=list(map(int,input().split()))
data+=[0 for _ in range(3-n)]
dp=[[[-1 for _ in range(61)] for _ in range(61)] for _ in range(61)]
q=deque()
dp[data[0]][data[1]][data[2]]=0
q.append(data+[0])
while True:
    *nums,count=q.popleft()
    if all(i==0 for i in nums):
        print(dp[0][0][0])
        break
    for dx in permutations([9,3,1]):
        temp=copy.deepcopy(nums)
        for i in range(3):
            temp[i]-=dx[i]
            if temp[i]<=0:
                temp[i]=0
        if dp[temp[0]][temp[1]][temp[2]]==-1:
            dp[temp[0]][temp[1]][temp[2]]=count+1
            q.append([temp[0],temp[1],temp[2],count+1])