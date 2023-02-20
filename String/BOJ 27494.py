def check(n):
    data=list(str(n))
    m=len(data)
    for i in range(m):
        if data[i]=='2':
            for j in range(i+1,m):
                if data[j]=='0':
                    for k in range(j+1,m):
                        if data[k]=='2':
                            for a in range(k+1,m):
                                if data[a]=='3':
                                    return 1
    return 0
n=int(input())
answer=0
for i in range(1,n+1):
    if i<2023:
        continue
    else:
        answer+=check(i)
print(answer)