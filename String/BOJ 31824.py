n,m=map(int,input().split())
data={}
for _ in range(n):
    a,b=input().split()
    data[a]=b

for _ in range(m):
    word=input()
    left=0
    right=0
    answer=""
    for i in range(len(word)):
        for j in range(i+1,len(word)+1):
            if word[i:j] in data:
                answer+=data[word[i:j]]
    if answer:
        print(answer)
    else:
        print(-1)