import sys
input=sys.stdin.readline
n=int(input())
data=[0 for _ in range(26)]
for _ in range(n):
    s=input().strip()
    temp=1
    for i in s[::-1]:
        j=ord(i)-ord('A')
        data[j]+=temp
        temp*=10
data=sorted(data,reverse=True)
answer=0
for i in range(9):
    answer+=data[i]*(9-i)
print(answer)