#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        @cache
        def dp(i: int, j: int) -> int:
            if i > j: return 0
            return max(dp(i, j - 1), nums[j] + dp(i, j - 2))
        return max(dp(0, len(nums) - 2), dp(1, len(nums) - 1))       
        
# @lc code=end

