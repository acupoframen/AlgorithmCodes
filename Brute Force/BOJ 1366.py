tune=['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']
n,m=map(int,input().split())
data=list(input().split())
code=list(input().split())
answer=1e10
for i in range(data):
    for j in code: