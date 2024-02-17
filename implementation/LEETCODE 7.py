class Solution:
    def reverse(self, x: int) -> int:

        neg=1
        if x<0:
            neg=-1
            x*=-1
        x=str(x)[::-1]
        if -2**31<=int(x)<=2**31-1:
            return neg*int(x)
        else:
            return 0
        