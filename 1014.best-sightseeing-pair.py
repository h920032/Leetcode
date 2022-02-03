#
# @lc app=leetcode id=1014 lang=python3
#
# [1014] Best Sightseeing Pair
#

# @lc code=start
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        @cache
        def dp(i: int) -> tuple:
            if i < 0: return (-10**9,-10**9)
            s, v = dp(i - 1)
            return (max(s, v + values[i] - i), max(v, values[i]+i))
        return dp(len(values)-1)[0]
        
# @lc code=end

