n=int(input())
chessBoard=[1e10]*n
ans=0
def dfs(idx):
    global ans
    if idx==n:
        ans+=1
        return
    for i in range(n):
        flag=0
        if i not in chessBoard:
            count=1
            while idx-count>=0:
                if chessBoard[idx-count]==i-count or chessBoard[idx-count]==i+count:
                    flag=1
                    break
                count+=1
            if not flag:
                count=1
                while idx+count<n:
                    if chessBoard[idx+count]==i-count or chessBoard[idx+count]==i+count:
                        flag=1
                        break
                    count+=1
            if not flag:
                chessBoard[idx]=i
                dfs(idx+1)
                chessBoard[idx]=1e10
dfs(0)
print(ans)



