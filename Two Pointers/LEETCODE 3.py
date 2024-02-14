class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        answer = 0
        charSet = set()
        l = 0
        for r in range(n):
            if s[r] not in charSet:
                charSet.add(s[r])
                answer = max(answer, r - l + 1)
            else:
                while s[r] in charSet:
                    charSet.remove(s[l])
                    l += 1
                charSet.add(s[r])
        
        return answer