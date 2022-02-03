#
# @lc app=leetcode id=1567 lang=python3
#
# [1567] Maximum Length of Subarray With Positive Product
#

# @lc code=start
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        @cache
        def dp(i: int) -> tuple:
            if i < 0: return (0,0)
            if i == 0: return (1 if nums[i] > 0 else 0, 1 if nums[i] < 0 else 0)
            max_p, max_n = dp(i - 1)
            if nums[i] > 0:
                return (max_p + 1, max_n + 1 if max_n > 0 else 0)
            elif nums[i] < 0:
                return (max_n + 1 if max_n > 0 else 0, max_p + 1)
            else:
                return (0, 0)
        return max(dp(i)[0] for i in range(len(nums)))

            


# @lc code=end

