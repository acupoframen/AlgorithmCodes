import sys
input=sys.stdin.readline
def checkDate(li):
    data=[]
    if 0<li[1]<=12:
        if 0<li[2]<=monthCheck(li[0],li[1]):
            data.append(li)
    if 0<li[1]<=12:
        if 0<li[0]<=monthCheck(li[2],li[1]):
            data.append([li[2],li[1],li[0]])
    if 0<li[0]<=12:
        if 0<li[1]<=monthCheck(li[2],li[0]):
            data.append([li[2],li[0],li[1]])
    if not data:
        print("invalid")
    else:
        safe=1
        for j in data:
            if today>j:
                safe=0
                break
        if safe:
            print("safe")
        else:
            print("unsafe")

def monthCheck(year,month):
    if month in [1,3,5,7,8,10,12]:
        return 31
    elif month==2:
        if not year%4:
            return 29
        else:
            return 28
    else:
        return 30

today=list(map(int,input().split()))
n=int(input())
for i in range(n):
    checkDate(list(map(int,input().split())))
