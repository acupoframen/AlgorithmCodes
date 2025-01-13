n=int(input())
answer=0
for _ in range(n):
    s=input()
    data=[]
    for i in range(len(s)):
        if data:
            if s[i]==data[-1]:
                data.pop()
            else:
                data.append(s[i])
        else:
            data.append(s[i])
    if not data:
        answer+=1
print(answer)