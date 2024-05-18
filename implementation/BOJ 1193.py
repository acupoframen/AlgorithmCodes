n=int(input())

for i in range(1,int(1e8)):
    if n>i:
        n-=i
        continue
    temp=i+1
    for j in range(1,i+1):
        temp-=1
        n-=1
        if not n:
            if i%2:
                print(f"{temp}/{i+1-temp}")
            else:
                print(f"{i+1-temp}/{temp}")
            exit(0)