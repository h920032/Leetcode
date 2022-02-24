#
# @lc app=leetcode id=740 lang=python3
#
# [740] Delete and Earn
#

# @lc code=start
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        f = {}
        m = 0
        for i in nums:
            if i in f: f[i] += i
            else:
                f[i] = i
                m = max(m,i)
        @cache
        def dp(i: int) -> int:
            if i <= 0: return 0
            if i in f:
                return max(dp(i - 1), dp(i - 2) + f[i])
            else:
                return max(dp(i - 1), dp(i - 2) + 0)
        return dp(m)

        
            
        
# @lc code=end

