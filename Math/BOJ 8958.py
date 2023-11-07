n=int(input())
for _ in range(n):
    s=input()
    answer=0
    currp=0
    for i in range(len(s)):
        if s[i]=='O':
            currp+=1
            answer+=currp
        else:
            currp=0
    print(answer)