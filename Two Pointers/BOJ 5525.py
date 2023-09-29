n=int(input())
m=int(input())
st=input()
left=0
right=0
count=0
while right<m:
    if st[right:right+3]=='IOI':
        right+=2
        if right -left== 2*n:
            count+=1
            left+=2
    else:
        right+=1
        left=right

print(count)