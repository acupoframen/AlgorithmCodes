n=int(input())
data=list(0 for _ in range(2))
for _ in range(n):
    temp=int(input())
    data[temp]+=1
if data[0] > data[1]:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")