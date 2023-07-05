n,s=map(int,input().split())
data=list(map(int,input().split()))
answer=0
halfn=n//2
left=[0 for _ in range(1<<(halfn))]
for i in range(1<<halfn):
    for j in range(halfn):
        if (i&(1<<j)) >0:
            left[i]+=data[j]

righthalfn=n-halfn
right=[0 for _ in range(1<<righthalfn)]
for i in range(1<<righthalfn):
    for j in range(righthalfn):
        if (i&(1<<j))>0:
            right[i]+=data[j+halfn]
left.sort()
right.sort(reverse=True)

i=0
j=0
while i<(1<<halfn) and j<(1<<righthalfn):
    if left[i] + right[j]==s:
        leftcount=1
        rightcount=1
        while i+1<(1<<halfn) and left[i]==left[i+1]:
            leftcount+=1
            i+=1
        while j+1<(1<<righthalfn) and right[j]==right[j+1]:
            rightcount+=1
            j+=1
        answer+=leftcount*rightcount
        i+=1
        j+=1
    elif left[i]+right[j]<s:
        i+=1
    else:
        j+=1
if s==0:
    print(answer-1)
else:
    print(answer)   
