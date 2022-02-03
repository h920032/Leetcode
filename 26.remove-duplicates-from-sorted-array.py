#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 0:
            return 0
        i = nums[0]
        s = 1
        for j in range(1,l):
            if nums[j] != i:
                i = nums[j]
                nums[s] = nums[j]
                s += 1
        return s
# @lc code=end

