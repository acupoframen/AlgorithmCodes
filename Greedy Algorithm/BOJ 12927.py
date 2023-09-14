data=[0]+list(input())
answer=0
for i in range(1,len(data)):
    if data[i]=='Y':
        for j in range(i,len(data),i):
            if data[j]=='Y':
                data[j]='N'
            else:
                data[j]='Y'
        answer+=1
print(answer)