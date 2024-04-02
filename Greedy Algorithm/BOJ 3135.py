a,b=map(int,input().split())
n=int(input())
data=list(int(input()) for _ in range(n))

curr=a
answer=0
for i in data:
    if abs(curr-b)>abs(b-i)+1:
        curr=i
if curr!=a:
    answer=1
print(answer+abs(curr-b))