t=int(input())
for _ in range(t):
    data=list(map(int,input().split()))
    data=data[1:]
    avg=sum(data)/len(data)
    ppl=0
    for i in range(len(data)):
        if data[i]>avg:
            ppl+=1
    print("%.3lf" %(100*ppl/len(data)),"%",sep="")