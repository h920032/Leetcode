#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        @cache
        def dp(i: int) -> tuple:
            if i == 0: return (nums[i], 0)
            p, n = dp(i - 1)
            max_p = max(p * nums[i], nums[i], n * nums[i])
            min_n = min(p * nums[i], nums[i], n * nums[i], 0)
            return (max_p, min_n)
        return max(dp(i)[0] for i in range(len(nums)))
        
# @lc code=end

