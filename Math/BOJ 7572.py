data=[]
for i in range(120):
    data.append([i%12,i%10])

n=int(input())
a,b=data[(n-4)%120]
print(chr(a+ord('A')),b,sep="")