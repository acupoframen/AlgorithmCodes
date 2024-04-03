n=int(input())
m=input()
k=int(input())
if m=='0':
    print("YES")
    exit(0)

for i in range(1,k+1):
    if i==n+1:
        print("YES")
        exit(0)
    if m[-i]=='1':
        print("NO")
        exit(0)
print("YES")