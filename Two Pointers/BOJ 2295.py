n=int(input())
data=list(int(input()) for _ in range(n))
data.sort()

def sol():
    while True:
        num=data.pop()
        for i in range(len(data)):
            left=i
            right=len(data)-1
            while left<=right:
                temp=data[i]+data[left]+data[right]
                if temp<num:
                    left+=1
                elif temp>num:
                    right-=1
                else:
                    return temp

print(sol())