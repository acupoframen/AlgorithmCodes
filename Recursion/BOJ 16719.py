s=input()
visited=[0 for _ in range(len(s))]
def calc(start,end):
    if start==end:
        return
    i=start
    temp=s[start:end]
    temp=sorted(temp)
    for j in range(start,end):
        if temp[0]==s[j] and not visited[j]:
            visited[j]=1
            start=j+1
            break
    for j in range(len(s)):
        if visited[j]==1:
            print(s[j],end="")
    print()
    calc(start,end)
    calc(i,start-1)
calc(0,len(s))