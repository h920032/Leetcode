#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        result = [1] * l
        p_1, p_2 = 1, 1
        for i in range(1, l):
            p_1 *= nums[i - 1]
            result[i] *= p_1
            p_2 *= nums[-i]
            result[-1-i] *= p_2
        return result

# @lc code=end

