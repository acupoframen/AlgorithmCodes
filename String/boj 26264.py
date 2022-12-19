n=int(input())
string=input()
count=0
for i in string:
    if i=='s':
        count+=1
    if i=='b':
        count-=1
if count>0:
    print("security!")
elif count<0:
    print("bigdata?")
else:
    print("bigdata? security!")
