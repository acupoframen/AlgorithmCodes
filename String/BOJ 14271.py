n,m=map(int,input().split())
data=list(input() for _ in range(n))
answer=0
answerst=''
for j in range(m):
    temp=[0,0,0,0]
    for i in range(n):
        if data[i][j]=='A':
            temp[0]+=1
        elif data[i][j]=='C':
            temp[1]+=1
        elif data[i][j]=='G':
            temp[2]+=1
        else:
            temp[3]+=1

    temp1=temp.index(max(temp))

    answer+=n-max(temp)
    if temp1==0:
        answerst+='A'
    elif temp1==1:
        answerst+='C'
    elif temp1==2:
        answerst+='G'
    else:
        answerst+='T'
print(answerst)
print(answer)