import sys
def hanoi(n, k, source, target, temp):
    if n == 1:    
        return (source, target)
    else:
        m = (1 << (n -1)) -1 
        if k<=m:
            return hanoi(n-1, k, source, temp, target)
        elif k == m+1:
            return (source, target)
        else:
            return hanoi(n-1,k -(m +1), temp, target, source)
n,k =map(int,input().split())
move = hanoi(n, k, 1, 3, 2)
print(move[0], move[1])