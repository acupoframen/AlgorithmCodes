m=int(1e6)
p=15*pow(10,5)
fibo=[0,1]
for i in range(2,p):
    fibo.append(fibo[i-2]+fibo[i-1])
    fibo[i]%=m
print(fibo[int(input())%p])