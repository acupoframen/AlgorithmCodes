import sys
input = sys.stdin.readline
t=int(input())
for _ in range(t):  
    s=input()
    data=[]
    temp=0
    for i in s:
        if i in ['a','e','i','o','u']:
            data.append(temp)
            temp=0
        else:
            temp+=1
    answer=1
    data.append(temp)
    if len(data)==1:
        print(-1)
        continue
    elif len(data)==2:
        print(1)
        continue
    else:
        for i in range(1,len(data)-1):
            answer*=(data[i]+1)
            answer%=(10**9+7)
    print(answer)