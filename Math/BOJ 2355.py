a,b=map(int,input().split())
a,b=min(a,b),max(a,b)
answer=0
answer+=(b)*(b+1)//2
answer-=(a-1)*(a)//2
print(answer)