class Solution:
    def longestPalindrome(self, s: str) -> str:
        l=len(s)
        answer=s[0]
        tempanswer=s[0]
        for i in range(l-1):
            if s[i]==s[i+1]:
                tempanswer=s[i:i+2]
                k=1
                while i-k>=0 and i+1+k<=l-1:
                    if s[i-k]==s[i+1+k]:
                        tempanswer=s[i-k]+tempanswer+s[i+1+k]
                        k+=1
                    else:
                        break    
            k=1
            tempanswer2=s[i]
            while i-k>=0 and i+k<=l-1:
                if s[i-k]==s[i+k]:
                    tempanswer2=s[i-k]+tempanswer2+s[i+k]
                    k+=1
                else:
                    break
            tempanswer=tempanswer if len(tempanswer)>len(tempanswer2) else tempanswer2
            if len(answer)<len(tempanswer):
                answer=tempanswer
        return answer