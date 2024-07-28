n,k,q=map(int,input().split())
count=[]
person=[]
check=[0 for _ in range(26)]
for _ in range(k):
    a,b=input().split()
    count.append(int(a))
    person.append(b)
q-=1
if count[q]==0:
    print(-1)
    exit(0)
for i in range(k):
    if count[q]<=count[i]:
        check[ord(person[i])-ord('A')]=1
check[0]=1
for i in range(n):
    if not check[i]:
        print(chr(i+ord('A')),end=" ")