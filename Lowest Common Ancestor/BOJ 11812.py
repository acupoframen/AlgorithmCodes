n,k,q=map(int,input().split())
def parents(x):
    return (x-2)//k+1
def lca(x,y):
    d=0
    while x!=y:
        if x>y:
            x=parents(x)
        else:
            y=parents(y)
        d+=1
    return d
for _ in range(q):
    x,y=map(int,input().split())
    if k==1:
        print(abs(x-y))
        continue
    print(lca(x,y))