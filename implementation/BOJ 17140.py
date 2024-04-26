import sys
from collections import Counter
input = sys.stdin.readline
r,c,k=map(int, input().split())
data = []
for _ in range(3):
    data.append(list(map(int, input().split())))
def rc():
    max_len = 0
    for j in range(len(data)):
        a = [i for i in data[j] if i!= 0]
        a = Counter(a).most_common() 
        a.sort(key = lambda x: (x[1], x[0])) 
        data[j] = [] 
        for key, value in a:
            data[j].append(key)
            data[j].append(value)
        if max_len < len(a) * 2:
            max_len = len(a) * 2
    for j in range(len(data)):
        for k in range(max_len - len(data[j])):
            data[j].append(0)
        data[j] = data[j][:100]
for i in range(101):
    try:
        if data[r-1][c-1]==k:
            print(i)
            break
    except:
        pass
    if len(data) < len(data[0]):
        data = list(zip(*data))
        rc()
        data = list(zip(*data))
    else:
        rc()
else:
    print(-1)