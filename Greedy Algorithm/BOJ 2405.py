n=int(input())
data=list(int(input()) for _ in range(n))
data.sort()
answer=-1e10
for i in range(n-1):
    answer=max(answer,abs(data[i]-2*data[i+1]+data[-1]))
for i in range(1,n-1):
    answer=max(answer,abs(data[0]-2*data[i]+data[i+1]))
print(answer)