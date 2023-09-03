n,l=map(int,input().split())
data=[list(map(int,input().split())) for _ in range(n)]
answer=0
def check(line):
    global l
    visited=[False for _ in range(n)]
    for i in range(0,n-1):
        if line[i]==line[i+1]:
            continue
        elif abs(line[i]-line[i+1])>1:
            return False
        elif line[i]>line[i+1]:
            temp=line[i+1]
            for j in range(i+1,i+l+1):
                if 0<=j<n:
                    if temp!=line[j]:
                        return False
                    elif visited[j]:
                        return False
                    visited[j]=True
                else:
                    return False
        else:
            temp=line[i]
            for j in range(i,i-l,-1):
                if 0<=j<n:
                    if temp!=line[j]:
                        return False
                    elif visited[j]:
                        return False
                    visited[j]=True
                else:
                    return False
    return True

for i in data:
    if check(i):
        answer+=1

for i in range(n):
    temp=[]
    for j in range(n):
        temp.append(data[j][i])
    if check(temp):
        answer+=1
print(answer)