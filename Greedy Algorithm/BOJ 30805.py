n=int(input())
data1=list(map(int,input().split()))
m=int(input())
data2=list(map(int,input().split()))
common=set(data1)&set(data2)
answer=[]
while common:
    maxval=max(common)
    answer.append(maxval)
    idx1=data1.index(maxval)
    idx2=data2.index(maxval)
    data1=data1[idx1+1:]
    data2=data2[idx2+1:]
    common=set(data1) & set(data2)
print(len(answer))
if answer:
    print(*answer)