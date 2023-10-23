n=int(input())
start=1
if n==1:
    print(1)
    exit(0)
answer=1
for i in range(6,int(1e10),6):
    if start<n<=start+i:
        print(answer+1)
        exit(0)
    answer+=1
    start+=i