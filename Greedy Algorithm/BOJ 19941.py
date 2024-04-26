n,k=map(int,input().split())
s=list(input())
answer=0
for i in range(n):
    if s[i]=='P':
        for j in range(max(0,i-k),min(i+k+1,n)):
            if s[j]=='H':
                s[j]='X'
                answer+=1
                break
print(answer)