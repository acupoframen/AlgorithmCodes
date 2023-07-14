from collections import deque
t=int(input())
for _ in range(t):
    data=[' ' for _ in range(10000)]
    start,end=map(int,input().split())
    time=0
    data[start]=''
    q=deque([start])
    while q:
        num=q.popleft()
        if num==end:
            break
        newnum=(num*2)%10000
        if data[newnum]==' ':
            data[newnum]=data[num]+'D'
            q.append(newnum)
        if num!=0:
            newnum=num-1
        else:
            newnum=9999
        if data[newnum]==' ':
            data[newnum]=data[num]+'S'
            q.append(newnum)
        newnum=(num//1000)+(num%1000)*10
        if data[newnum]==' ':
            data[newnum]=data[num]+'L'
            q.append(newnum)

        newnum= (num%10)*1000+(num//10)
        if data[newnum]==' ':
            data[newnum]=data[num]+'R'
            q.append(newnum)
    print(data[end])
