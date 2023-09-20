data=list(map(int,input().split()))
answer=0
for i in range(5):
    answer+= data[i]**2
print(answer%10)