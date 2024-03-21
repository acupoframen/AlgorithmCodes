a,b=map(int,input().split())
if a>b:
    print(2*(a-b)//b)
else:
    print(2*(b-a)//b)