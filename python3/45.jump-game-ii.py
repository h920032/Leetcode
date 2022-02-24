#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def dp(i: int) -> bool:
            if i >= n - 1: return 0
            if i + nums[i] >= n - 1: return 1
            ans = n
            for j in range(1, nums[i] + 1):
                ans = min(ans,dp(i + j) + 1)
            return ans
        return dp(0)

# @lc code=end

