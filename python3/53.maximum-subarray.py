#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = nums[0]
        max_sum = nums[0]
        for i in range(1,len(nums)):
            if nums[i] >= current + nums[i]:
                current = nums[i]
            else:
                current += nums[i]
            if current > max_sum:
                max_sum = current
        return max_sum

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def dp(i: int) -> int:
            if i == 0: return nums[0]
            return max(nums[i] + dp(i - 1), nums[i])
        return max(dp(i) for i in range(len(nums)))
# @lc code=end

