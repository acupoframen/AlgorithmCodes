n=int(input())
answer=""
while n:
    div,mod=divmod(n,3)
    answer+=str(mod)
    n//=3
if '2' in str(answer[::-1]) or not answer:
    print("NO")
else:
    print("YES")