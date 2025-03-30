from collections import defaultdict
t=int(input())
for _ in range(t):
    n=int(input())
    data=list(map(int,input().split()))
    d=defaultdict(int)
    for i in range(n):
        d[data[i]]+=1
    exception=[]
    for i in d.keys():
        if d[i]!=6:
            exception.append(i)
    answer=[]
    p=defaultdict(list)
    temp=1
    for i in range(n):
        if data[i] in exception:
            continue
        p[data[i]].append(temp)
        temp+=1

    for i in p.keys():
        answer.append([sum(p[i][:4]),p[i][4],i])
    answer.sort(key=lambda x:(x[0],x[1]))
    print(answer[0][2])


