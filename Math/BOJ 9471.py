t=int(input())
def  calc(num):
    answer=1
    mod1,mod2=1,2
    while True:
        if mod1%num==1 and mod2%num==1:
            break
        answer+=1
        mod1,mod2=mod2,(mod1+mod2)%num
    return answer
for _ in range(t):
    a,b=map(int,input().split())
    print(a,calc(b))