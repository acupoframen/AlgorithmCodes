n=int(input())
data=list(input() for _ in range(n))
answer=0
for i in range(n):
    for j in range(i+1,n):
        a=data[i]
        b=data[j]
        for k in range(min(len(a),len(b))+1):
            if a[0:k+1]==b[-1:-k-2:-1][::-1] or b[0:k+1]==a[-1:-k-2:-1][::-1]:
                answer+=1
                break
print(answer)