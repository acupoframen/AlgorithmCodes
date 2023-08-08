import bisect
t=int(input())
n=int(input())
data1=list(map(int,input().split()))
m=int(input())
data2=list(map(int,input().split()))
sum1=[]
sum2=[]
for i in range(n):
    for j in range(i+1,n+1):
        sum1.append(sum(data1[i:j]))
for i in range(m):
    for j in range(i+1,m+1):
        sum2.append(sum(data2[i:j]))
sum2.sort()
answer=0
for i in range(len(sum1)):
    answer+=bisect.bisect_right(sum2,t-sum1[i])-bisect.bisect_left(sum2,t-sum1[i])
print(answer)