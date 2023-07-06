n=int(input())
equation=input()
answer=-1e10
def calculate(a,inte,b):
    if inte=="+":
        return int(a)+int(b)
    elif inte=='-':
        return int(a)-int(b)
    else:
        return int(a)*int(b)
def dfs(idx,past):
    global answer
    if idx>=n:
        answer=max(answer,past)
        return 
    if idx<n-3:
        dfs(idx+4, calculate(past,equation[idx],calculate(*equation[idx+1:idx+4])))
    dfs(idx+2,calculate(past,equation[idx],equation[idx+1]))

if n==1:
    print(equation[0])
else:
    dfs(1,equation[0])
    print(answer)