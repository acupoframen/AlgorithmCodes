from math import lcm

n=int(input())
data=list(map(lambda x: x*2,map(int,input().split())))
print(lcm(*data))