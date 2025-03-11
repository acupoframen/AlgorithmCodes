import sys
input = sys.stdin.readline
n = int(input())
data = sorted(map(int, input().split()) ,reverse=True)
if n == 1:
    print(1)
elif data[0] <= sum(data[1:])+1:
    print(sum(data))
else:
    print(sum(data[1:])*2+1)