#
# @lc app=leetcode id=410 lang=python3
#
# [410] Split Array Largest Sum
#

# @lc code=start
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        prefix_sum = [0] + list(itertools.accumulate(nums))
        l = len(nums)
        @cache
        def dp(n, m):
            if m == 1: return prefix_sum[l] - prefix_sum[n]
            min_s = prefix_sum[l]
            for i in range(n, l - m + 1):
                first_split_sum = prefix_sum[i + 1] - prefix_sum[n]
                min_s = min(min_s, max(first_split_sum, dp(i + 1 ,m - 1)))
                if first_split_sum >= min_s:
                    break
            return min_s
        return dp(0, m)
                
# @lc code=end

