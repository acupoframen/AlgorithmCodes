from itertools import product
n,m=map(int,input().split())
tones=list(("A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"))
current=list(input().split())
code=list(input().split())
answer=1e10
for goal in product(range(m),repeat=n):
    if len(set(goal))!=m:
        continue
    flats=[]
    for k in range(n):
        number=0
        currenttone=tones.index(current[k])
        if tones[currenttone]==code[goal[k]]:
            continue
        while tones[(currenttone+number)%12]!=code[goal[k]]:
            number+=1
        flats.append(number)
    if flats:
        temp=[]
        temp.append(max(flats)-min(flats)+1)
        flats.sort()
        for i in range(1, len(flats)):
            temp.append(1+flats[i-1]+12-flats[i])
        answer=min(answer,min(temp))
    else:
        answer=0
print(answer)