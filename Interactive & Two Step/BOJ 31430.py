T=int(input())
if T==1:
    a,b=map(int,input().split())
    a+=b
    temp=""
    while a:
        temp=chr(a%26+ord('a'))+temp
        a//=26
    while len(temp)!=13:
        temp='a'+temp
    print(temp)
else:
    a=input()
    temp=0
    val=1
    for i in range(12,-1,-1):
        temp+=val*(ord(a[i])-ord('a'))
        val*=26
    print(temp)