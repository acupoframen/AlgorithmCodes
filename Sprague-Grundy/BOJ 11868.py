n=int(input())
data=list(map(int,input().split()))
x=0
for i in range(n):
    x^=data[i]

if x:
    print("koosaga")
else:
    print("cubelover")