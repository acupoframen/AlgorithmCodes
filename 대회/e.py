n=int(input())
data=input()
m=int(input())
code=[[] for _ in range(26)]
for i in range(m):
    a,b=list(input())
    code[ord(a)-ord('a')].append(ord(b)-ord('a'))

