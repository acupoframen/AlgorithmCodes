n=int(input())
answer=0
while True:
    if not n%5:
        answer+=n//5
        break
    elif (0<n<3):
        answer=-1
        break
    else:
        n-=3
        answer+=1

print(answer)