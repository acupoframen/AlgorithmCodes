from itertools import permutations
n=int(input())
k=int(input())
data=list(input() for _ in range(n))
answer=[]
for i in permutations(range(n),k):
    temp=""
    for k in i:
        temp+=data[k]
    answer.append(temp)
print(len(set(answer)))
