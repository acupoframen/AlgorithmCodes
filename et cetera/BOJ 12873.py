n=int(input())
data=[i for i in range(n)]
loc=0
for i in range(1,n):
    num=i**3%len(data)-1
    if loc+num>=len(data):
        loc=num-(len(data)-loc)
    else:
        loc=loc+num
    del data[loc]
    if loc==len(data) or loc==-1:
        loc=0
print(data[0]+1)