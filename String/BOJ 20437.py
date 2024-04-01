t=int(input())
for i in range(t):
    data=[[] for _ in range(26)]
    n=input()
    num=int(input())
    for i in range(len(n)):
        ch=ord(n[i])-ord('a')
        data[ch].append(i)
    
    minval=1e10
    maxval=0
    for i in range(26):
        if len(data[i])>=num:
            for j in range(len(data[i])-num+1):
                minval=min(minval,data[i][j+num-1]-data[i][j]+1)
                maxval=max(maxval,data[i][j+num-1]-data[i][j]+1)
    if minval==1e10:
        print(-1)
        continue
    print(minval,maxval)