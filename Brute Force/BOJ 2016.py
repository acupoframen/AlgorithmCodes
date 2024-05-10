from itertools import permutations
t=int(input())
def calc(temp):
    current=[0 for _ in range(11)]
    chosen=[[] for _ in range(11)]
    while not all(current[1:]):
        for woman in range(6,11):
            if current[woman]==0:
                preferredman=temp[woman]
                for i in preferredman:
                    if i not in chosen[woman]:
                        chosen[woman].append(i)
                        if current[i]==0: 
                            current[i]=woman
                            current[woman]=i
                            break
                        elif temp[i].index(current[i])>temp[i].index(woman):
                            current[current[i]]=0
                            current[woman]=i
                            current[i]=woman
                            break
    return current[1]
for _ in range(t):
    data=list(list(map(int,input().split())) for _ in range(9))
    answer=0
    flag=0
    for k in permutations([6,7,8,9,10],5):
        temp=[[0]]+[list(k)]+data
        if list(k)==[6,7,8,9,10]:
            answer=calc(temp)
        else:
            val=calc(temp)
            if val<answer:
                print("YES")
                flag=1
                break
    if not flag:
        print("NO")
