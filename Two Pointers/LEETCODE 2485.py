class Solution:
    def pivotInteger(self, n: int) -> int:
        temp=0
        a=1
        b=n
        while a!=b:
            if temp>=0:
                temp-=a
                a+=1
            else:
                temp+=b
                b-=1
        if not temp:
            return a
        else:
            return -1