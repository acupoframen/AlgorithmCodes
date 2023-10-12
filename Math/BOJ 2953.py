data=[]
for i in range(5):
    data.append([i,sum(list(map(int,input().split())))])

data.sort(key=lambda x: (x[1],x[0]))

print(data[4][0]+1, data[4][1])