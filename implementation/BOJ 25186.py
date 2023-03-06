n=int(input())
data=list(map(int,input().split()))
data.sort(reverse=True)
if n==1:
    if data[0]==1:
        print("Happy")
    else:
        print("Unhappy")
elif data[0]>sum(data[1:]):
    print("Unhappy")
else:
    print("Happy")