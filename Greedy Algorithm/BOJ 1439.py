s=input()
arr=[0,0]
curr=int(s[0])
arr[curr] += 1
for i in s[1:]:
    if curr!=int(i):
        arr[int(i)] += 1
        curr=int(i)

print(min(arr))