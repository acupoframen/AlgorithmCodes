n=int(input())
answer=0
for _ in range(n):
    alphabets=[0 for _ in range(26)]
    
    word=input()
    pastWord=word[0]
    okayflag=1
    alphabets[ord(word[0])-ord('a')]=1
    if len(word)==1:
        answer+=1
        continue
    else:
        for i in word[1:]:
            if i==pastWord:
                pass
            else:
                if alphabets[ord(i)-ord('a')]==1:
                    okayflag=0
                    break
                else:
                    pastWord=i
                    alphabets[ord(i)-ord('a')]=1
            if not okayflag:
                break
        if okayflag:
            answer+=1

print(answer)