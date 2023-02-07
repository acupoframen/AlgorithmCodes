n=int(input())
data=list(map(int,input().split()))
stacks=[[0] for _ in range(4)]
goal=n
for i in range(n): 
    for s in stacks:
        appendCheck=0
        if s[len(s)-1]<data[i]:
            s.append(data[i])
            appendCheck=1
            break
    if not appendCheck:
        print("NO")
        exit(0)
while goal!=0:
    goal-=1
    if goal==0:
        print("YES")
        exit(0)
    popCheck=0
    for s in stacks:
        if s[len(s)-1]==goal:
            popCheck=1
            s.pop()
            break
print("YES")