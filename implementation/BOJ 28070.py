n=int(input())

start=list(0 for _  in range(10001*12))
end=list(0 for _ in range(10001*12))

for _ in range(n):
    a,b=input().split()
    a1,a2=map(int,a.split("-"))
    b1,b2=map(int,b.split("-"))
    start[a1*12+a2]+=1
    end[b1*12+b2]+=1
answer=-1
temp=0
when=0
for i in range(2000*12,10001*12):
    temp+=start[i]
    if temp>answer:
        when=i
        answer=temp
    temp-=end[i]

if not when%12:
    print(f"{(when//12)-1}-12")
else:
    print(f"{when//12}-%02d" %(when%12))
