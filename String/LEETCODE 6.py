class Solution:
    def convert(self, s: str, numRows: int) -> str:
        data=list([] for _ in range(numRows))
        temp=0
        down=1
        for i in s:
            data[temp].append(i)
            if temp==0:
                down=1
            elif temp==numRows-1:
                down=-1
            if numRows==1:
                down=0
            temp+=down
        answer=''
        for i in data:
            answer+=''.join(i)
        return answer