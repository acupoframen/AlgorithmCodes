import math
from collections import defaultdict

n = int(input())
s, answer, sumlist = [], [], []
freq = defaultdict(int)

s=list(map(int,input().split()))
s.sort()

answer.append(s[1])
if n == 1:
    
    print(*answer)
    exit(0)

answer.append(s[2])
if n == 2:
    print(*answer)
    exit(0)
sumlist.append(0)
sumlist.append(s[1])
sumlist.append(s[2])
sumlist.append(s[1] + s[2])
freq[s[1] + s[2]] += 1
for i in range(3, len(s)):
    if len(answer)==n:
        break
    if freq[s[i]] == 0:
        newsumlist=sumlist[:]
        for j in range(len(sumlist)):
            y=sumlist[j]+s[i]
            newsumlist.append(y)
            if j != 0:
                freq[y] += 1
        sumlist = newsumlist
        answer.append(s[i])
    else:
        freq[s[i]]-= 1
print(*sorted(answer))
