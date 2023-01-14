n=int(input())
data=list(map(int,input().split()))
needed=[]
needed.append(min(data[0],data[5]))
needed.append(min(data[1],data[4]))
needed.append(min(data[2],data[3]))
needed.sort()
answer=0
if n==1:
    answer=sum(sorted(data)[0:5])
else:
    answer+=4*(n-1)*sum(needed[0:2])
    answer+=4*(n-2)*sum(needed[0:2])
    answer+=4*(n-1)*(n-2)*needed[0]
    answer+=(n-2)*(n-2)*needed[0]
    answer+=4*sum(needed)
print(answer)