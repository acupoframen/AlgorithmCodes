while True:
    n=int(input())
    if n==0:
        break
    data=[]
    while n>0:
        data.append(n%10)
        n//=10
    answerFlag=True
    for i in range(len(data)):
        if data[i]!=data[len(data)-i-1]:
            answerFlag=False
            break
    if answerFlag:

        print("yes")
    else:
        print("no")