s=list(input())
t=list(input())
def dfs(s,t):
    if s==t:
        return True
    elif len(t)==len(s):
        return False
    answer=0
    if t[-1]=='A':
        answer=dfs(s,t[:-1])
    if answer==1:
        return True
    if t[0]=='B':
        answer=dfs(s,t[::-1][:-1])
    return answer
if dfs(s,t):
    print(1)
else:
    print(0)