n=input()
count=0
while int(n)>=10:
    n=str(sum(list(map(int,n))))
    count+=1
print(count)
if int(n)%3:
    print("NO")
else:
    print("YES")