n=int(input())
data=list(map(int,input().split()))

if sum(data)==0:
    print(0)
    exit(0)
data=list(map(str,data))
data.sort(key= lambda x: x*9 , reverse=True)
print(*data, sep="")