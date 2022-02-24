#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        @cache
        def dp(i: int) -> bool:
            if i >= n - 1: return True
            if i + nums[i] >= n - 1: return True
            for j in range(1, nums[i] + 1):
                if dp(i + j): return True
            return False
        return dp(0)
        
# @lc code=end

