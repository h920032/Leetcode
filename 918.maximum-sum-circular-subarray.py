#
# @lc app=leetcode id=918 lang=python3
#
# [918] Maximum Sum Circular Subarray
#

# @lc code=start
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def dp(i: int, s: int) -> int:
            if i == 0:return nums[i] * s
            return max(nums[i] * s, dp(i - 1, s) + nums[i] * s)
        max_n = sum(nums) + max(dp(i, -1) for i in range(n))
        max_p = max(dp(i, 1) for i in range(n))
        if max_n == 0:
            return max_p
        return max(max_n, max_p)
# @lc code=end

