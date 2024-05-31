k,n=map(int,input().split())
data=list(int(input()) for _ in range(k))
for _ in range(n-k):
    data.append(max(data))
data=list(map(str,data))
data.sort(key=lambda x: x*10, reverse=True)
print(''.join(data))