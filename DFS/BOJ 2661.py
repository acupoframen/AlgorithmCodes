def goodCheck(arr):
    for i in range(1,len(arr)//2+1):
       if arr[len(arr)-i:len(arr)]==arr[len(arr)-2*i:len(arr)-i]:
           return False
    return True
def dfs(arr,idx):
    if idx==n:
        arr=list(map(str,arr))
        print(''.join(arr ))
        exit()
    for i in range(1,4):
        if goodCheck(arr+[i]):
            arr.append(i)
            dfs(arr,idx+1)
            arr.pop()
    
            
n=int(input())
dfs([],0)
