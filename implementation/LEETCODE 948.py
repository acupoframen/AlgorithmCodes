from collections import deque
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        answer=0
        tokens.sort()
        q=deque()
        for i in tokens:
            q.append(i)
        print(q)
        
        while q:
            if power>=q[0]:
                power-=q.popleft()
                answer+=1
            elif len(q)>=2 and answer>0:
                power-=q.popleft()
                power+=q.pop()
            else:
                break

        
        return answer