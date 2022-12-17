n,m=map(int,input().split())
if n*m%2==1:
    print(-1)
else:
    data=[]
    dx=[[0,1],[1,0]]
    flag=1
    count=0
    for i in range(n):
        data.append(list(map(int,input().split())))
    sumList=0
    for i in range(n):
        sumList+=sum(data[i])
    if not sumList%2:
        for i in range(n-1):
            for j in range(m-1):
                for k in range(2):
                    if data[i][j]+data[i+dx[k][1]][j+dx[k][0]]==0 or 2:
                        print(1)
                        flag=0
                        break
                    if flag==0:
                        break
                if flag==0:
                    break
            if flag==0:
                break
    if flag==1:
        print(-1)
