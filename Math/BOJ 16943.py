from itertools import permutations
a,b=input().split()
answer=-1
for i in permutations(a):
    
    num = int(''.join(i))
    if num < int(b) and i[0] != '0':
        answer = max(answer, num)
print(answer)