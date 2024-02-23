import sys
sys.setrecursionlimit(int(1e5+1))
n=int(input())
inorder=list(map(int,input().split()))
posorder=list(map(int,input().split()))
inorderidx=[0 for _ in range(n+1)]
for i in range(n):
    inorderidx[inorder[i]]=i

def preorder(inleft,inright,postleft,postright):
    if inleft>inright or postleft>postright:
        return
    root= posorder[postright]
    print(root,end=' ')
    inroot= inorderidx[root]
    left=inroot - inleft
    preorder(inleft, inroot-1, postleft, postleft+left-1)
    right= inright- inroot
    preorder(inroot+1, inright, postright-right,postright-1)

preorder(0,n-1,0,n-1)