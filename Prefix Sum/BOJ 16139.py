import sys
input=sys.stdin.readline
string=input().strip()
q=int(input())
counts=list(list(0 for _ in range(26)) for _ in range(len(string)+1))
for i in range(len(string)):
    for j in range(26):
        if j==ord(string[i])-ord('a'):
            counts[i+1][j]=counts[i][j]+1
        else:
            counts[i+1][j]=counts[i][j]
for _ in range(q):
    c,l,r=input().strip().split()
    l=int(l)
    r=int(r)
    print(counts[r+1][ord(c)-ord('a')]-counts[l][ord(c)-ord('a')])