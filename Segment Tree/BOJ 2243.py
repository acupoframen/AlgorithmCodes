n=int(input())

data=[0]*(10**6+1)
tree=[0]*(2**22)

def changeval(target, difference, index, start, end):
    if end<target or target<start:
        return
    tree[index]+=difference
    if start!=end:
        changeval(target,difference,index*2,start,(start+end)//2)
        changeval(target,difference, index*2+1, (start+end)//2+1,end)

def printval(count,index,start,end):
    if start==end:
        return end
    else:
        if tree[index*2]>=count:
            return printval(count,index*2,start,(start+end)//2)
        else:
            return printval(count-tree[index*2],index*2+1,(start+end)//2+1,end)

for _ in range(n):
    a,*b=map(int,input().split())
    
    if a==1:
        b=b[0]
        answer=printval(b,1,1,10**6)
        print(answer)
        changeval(answer,-1,1,1,10**6)
        data[answer]-=1

    else:
        b,c=b
        changeval(b,c,1,1,10**6)
        data[b]+=c
        