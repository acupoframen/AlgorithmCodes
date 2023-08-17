def check(num):
    if len(num)==1:
        return True
    for i in range(len(num)//2):
        if num[i]==num[len(num)-i-1]:
            return False
    return check(num[0:len(num)//2]) and check(num[len(num)//2+1:len(num)])
t=int(input())
for _ in range(t):
    num=list(input())
    if check(num):
        print("YES")
    else:
        print("NO")