def f(x,y):
    temp=abs(data[x][0]-data[y][0])+abs(data[x][1]-data[y][1])
    return temp

def solve(m,n):
    temp=0
    next = max(m,n)+1
    if next == w+2:
        return 0
    if dp[m][n]!=-1:
        return dp[m][n]
    val1 = solve(next,n)+f(m,next)
    val2 = solve(m,next)+f(n,next)
    if val1 < val2:
        dplog[m][n]=1
        dp[m][n]=val1
    else :
        dplog[m][n]=2
        dp[m][n]=val2
    temp = dp[m][n]
    return temp

n=int(input())
w =int(input())
data = [[1,1],[n,n]]
for _ in range(w):
    data.append(list(map(int,input().split())))
dp = list(list(-1 for _ in range(1002)) for _ in range(1002))
dplog =list(list(-1 for _ in range(1002)) for _ in range(1002))
print(solve(0,1))
m=0
n=1
for i in range(2,w+2):
    print(dplog[m][n])
    if dplog[m][n]==1:
        m=i
    else:
        n=i