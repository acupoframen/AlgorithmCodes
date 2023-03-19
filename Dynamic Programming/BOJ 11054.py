n=int(input())
increasedp=[1 for _ in range(n)]
decreasedp=[1 for _ in range(n)]
data=list(map(int,input().split()))
for i in range(n):
   for j in range(i):
      if data[i]>data[j]:
         increasedp[i]=max(increasedp[i],increasedp[j]+1)
for i in range(n-1,-1,-1):
   for j in range(i+1,n):
      if data[i]>data[j]:
         decreasedp[i]=max(decreasedp[i],decreasedp[j]+1)
answer=0
for i in range(n):
   answer=max(answer,increasedp[i]+decreasedp[i])
print(answer-1)