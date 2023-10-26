n=int(input())
data=list(map(lambda x: (ord(x)-ord('a')+1),list(input())))

answer=0
for i in range(n):
    answer+=31**i*data[i]
print(answer%1234567891)