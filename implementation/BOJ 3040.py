data=list(int(input()) for _ in range(9))
temp=sum(data)-100
data.sort()
for i in range(8):
    for j in range(i+1,9):
        if data[i]+data[j]==temp:
            for k in range(9):
                if k!=i and k!=j:
                    print(data[k])