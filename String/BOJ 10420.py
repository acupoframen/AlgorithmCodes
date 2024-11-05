n=int(input())

def yun(k):
    if not k%400 or (not k%4 and k%100):
        return True
    else:
        return False

months=[0,31,28,31,30,31,30,31,31,30,31,30,31]

year=2014
month=5
if n<=29:
    print("2014-04-%02d" %(1+n))
    exit(0)
n-=29
while True:
    if yun(year):
        months[2]=29
    else:
        months[2]=28
    while month<13:
        if n<=months[month]:
            print("%d-%02d-%02d" %(year,month,n))
            exit(0)
        n-=months[month]
        month+=1
    year+=1
    month=1