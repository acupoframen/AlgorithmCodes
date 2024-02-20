class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        data=list(0 for i in range(len(nums)+1))
        for i in nums:
            data[i]+=1
        return data.index(0)