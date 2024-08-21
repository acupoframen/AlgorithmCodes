from collections import defaultdict
n=int(input())
data=defaultdict(list)
prices=defaultdict(int)
for _ in range(n):
    s,w,d,p=input().split()
    w=int(w)
    d=int(d)
    p=int(p)
    data[w*7+d].append([s,p])

answer=0
for _ in range(n):
    s,p=input().split()
    prices[s]=int(p)

temp=0
for i in range(100):
    if i in data.keys():
        flag=1
        for j in data[i]:
            if prices[j[0]]>=j[1]:
                temp+=1
                flag=0
                break
        if flag:
            temp=0
    else:
        temp=0
    answer=max(temp,answer)
print(answer)