x=int(input())
data=[]
while x!=0:
    remainder=x%2
    x//=2
    data.append(remainder)
print(sum(data))