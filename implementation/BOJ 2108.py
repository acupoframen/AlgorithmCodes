n=int(input())
data=[int(input()) for _ in range(n)]
print(round(sum(data)/n))
data.sort()
print(data[n//2])
newdata=[0 for _ in range(10001)]
for i in range(n):
    newdata[data[i]]+=1
freqdata=[]
for i in range(len(newdata)):
    if newdata[i]==max(newdata):
        if i>5000:
            freqdata.append(i-10001)
        else:
            freqdata.append(i)
freqdata.sort()
if len(freqdata)==1:
    print(freqdata[0])
else:
    print(freqdata[1])
print(max(data)-min(data))