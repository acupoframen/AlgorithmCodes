n,l=map(int,input().split())
data=list(list(input()) for _ in range(n))
for i in range(26): #얼마큼 바꿔줄건지
    for j in range(l): #어디를 바꿔줄건지
        correct=[0]*n
        temp=data[0][j]
        data[0][j]=chr(ord('A')+i)
        flag=0
        for k in range(1,n): #비교
            for a in range(l): 
                if data[0][a]!=data[k][a]:
                    correct[k]+=1
                    if correct[k]==2:
                        flag=1
                        data[0][j]=temp
                        break
                if flag==1:
                    break
            if flag==1:
                break
        if flag==1:
            continue
        else:
            for i in range(l):
                print(data[0][i],end='')
            exit(0)

print("CALL FRIEND")
        