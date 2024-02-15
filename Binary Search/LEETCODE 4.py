class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)
        n = n1 + n2
        l = (n1 + n2 + 1) // 2 
        low = 0
        high = n1        
        while low <= high:
            mid1 = (low + high) // 2 
            mid2 = l - mid1 
            l1 = -1e10
            l2 = -1e10
            r1 = 1e10
            r2 = 1e10
            if mid1 < n1:
                r1 = nums1[mid1]
            if mid2 < n2:
                r2 = nums2[mid2]
            if mid1 > 0:
                l1 = nums1[mid1-1]
            if mid2 > 0:
                l2 = nums2[mid2-1]
            if l1 <= r2 and l2 <= r1:
                if n % 2 == 1:
                    return max(l1, l2)
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2
            elif l1 > r2:
                high = mid1 - 1
            else:
                low = mid1 + 1