#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

1,2,3,4,5,
6,7,8,9,10

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = len(nums)
        flag = True
        i = 0
        j = l
        while flag:
            if i+1 == j:
                if nums[i] >= target:
                    return i
                else: return j
            middle = i + (j-i)//2
            if nums[middle] >= target:
                j = middle
            else:
                i = middle
            
        
# @lc code=end

