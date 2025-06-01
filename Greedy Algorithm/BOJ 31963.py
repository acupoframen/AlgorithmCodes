import math

n = int(input())   
arr = list(map(int, input().split()))  
tmp = 0 
cnt_arr = [0] * n  
for i in range(1, n):
    ratio = math.ceil(math.log2(arr[i - 1] / arr[i])) + cnt_arr[i - 1]
    if ratio > 0:
        cnt_arr[i] = max(0, ratio)  
        tmp += cnt_arr[i]  

print(tmp)