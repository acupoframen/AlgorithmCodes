k=int(input())
val=1
while 1:
    if val>=k:
        break
    else:
        val*=2
valsave=val
answer=0
while True:
    if k%val==0:
        break
    val//=2
    answer+=1

print(valsave,answer)