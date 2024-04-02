n=int(input())
answer=1
while True:
    s=str(answer)
    if n>len(s):
        n-=len(s)
        answer+=1
    else:
        print(s[n-1])
        exit(0)