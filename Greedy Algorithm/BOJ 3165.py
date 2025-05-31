n,k=map(int,input().split())
n+=1
nlist=list(str(n))
curridx=-1
maxidx=len(nlist)
while True:
    if nlist.count('5')>=k:
        break
    while nlist[curridx]=='5' and abs(curridx)<maxidx:
        curridx-=1
    currval=int(''.join(nlist))
    currval=currval+10**(abs(curridx)-1)
    nlist=list(str(currval))
    maxidx=len(nlist)
print(''.join(nlist))