t=int(input())
for _ in range(t):
    n=int(input())
    print(f"Pairs for {n}:",end=" ")
    answer=[]
    for k in range(1,n):
        if k>=n/2:
            break
        answer.append(f"{k} {n-k}")
    print(", ".join(answer))