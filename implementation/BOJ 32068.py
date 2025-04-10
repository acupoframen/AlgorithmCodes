t=int(input())
for _ in range(t):
    l,r,s=map(int,input().split())
    l-=s
    r-=s
    if l==0 or r==0:
        print(1)
        break
    answer=0
    if l>0:
        answer=l*2
    else:
        answer=-l*2+1
    if r>0:
        answer=min(answer,r*2)
    else:
        answer=min(answer,-l*2+1)
    print(answer)