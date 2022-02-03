#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 > n2:
            return self.findMedianSortedArrays(nums2,nums1)
        
        l = 0
        r = n1
        k = (n1 + n2 + 1) // 2

        while l < r:
            m1 = l + (r - l) // 2
            m2 = k - m1
            if nums1[m1] < nums2[m2 - 1]:
                l = m1 + 1
            else:
                r = m1
        m1 = l
        m2 = k - l

        c1 = max(float('-inf') if m1 <= 0 else nums1[m1 - 1],
                 float('-inf') if m2 <= 0 else nums2[m2 - 1])
        
        if (n1 + n2) % 2 == 1:
            return c1
        
        c2 = min(float('inf') if m1 >= n1 else nums1[m1],
                 float('inf') if m2 >= n2 else nums2[m2])
        
        return (c1 + c2) * 0.5
            
# @lc code=end

1,3,5,7,9,11,13,15 -> 7,9
8,10,12,14 -> 10,12

7,8,9,10,11,12

1,3,5,7,8,9,10,11,12,13,14,15