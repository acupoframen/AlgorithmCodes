numbers=list(sorted(map(int,input().split())))
abcdict={'A':numbers[0],'B':numbers[1],'C':numbers[2]}
for i in input():
    print(abcdict[i], end=' ')