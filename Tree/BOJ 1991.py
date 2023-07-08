n=int(input())
data=[[] for _ in range(n)]
for _ in range(n):
    a,b,c=map(lambda x: ord(x)-ord('A'),input().split())
    data[a].append(b)
    data[a].append(c)
def pre(i):
    print(chr(ord('A')+i),end='')
    if data[i][0]!=-19:
        pre(data[i][0])
    if data[i][1]!=-19:
        pre(data[i][1])
def mid(i):
    if data[i][0]!=-19:
        mid(data[i][0])
    print(chr(ord('A')+i),end='')
    if data[i][1]!=-19:
        mid(data[i][1])
def post(i):
    if data[i][0]!=-19:
        post(data[i][0])
    if data[i][1]!=-19:
        post(data[i][1])
    print(chr(ord('A')+i),end='')

pre(0)
print()
mid(0)
print()
post(0)