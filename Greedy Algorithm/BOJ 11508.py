n=int(input())
data=list(int(input()) for _ in range(n))
data.sort(reverse=True)
answer=0
for i in range(n):
    if i%3!=2:
        answer+=data[i]
print(answer)