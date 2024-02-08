t=int(input())
for _  in range(t):
    lena=int(input())
    a=list(map(int,input().split()))
    lenb=int(input())
    b=list(map(int,input().split()))
    lenc=int(input())
    c=list(map(int,input().split()))
    answer=[]
    for i in range(lena):
        for j in range(lenb):
            for k in range(lenc):
                temp=a[i]+b[j]+c[k]
                if not [i for i in str(a[i]+b[j]+c[k]) if i not in ['5','8']] and temp not in answer:
                    answer.append(temp)
    print(len(answer))