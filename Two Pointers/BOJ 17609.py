t=int(input())
for _ in range(t):
    data=list(input())
    l=len(data)
    i=0
    j=len(data)-1
    diffcount=0
    while i<=j:
        if data[i]==data[j]:
            i+=1
            j-=1
        else:
            if data[i+1:j+1]==data[i+1:j+1][::-1]or data[i:j]==data[i:j][::-1]:
                diffcount=1
            else:
                diffcount=2
            break
    
    print(diffcount)
            