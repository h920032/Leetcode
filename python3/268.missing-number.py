#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        s = ((0 + l) * (l + 1)) // 2
        for n in nums:
            s -= n
        return s

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        for i, n in enumerate(nums):
            l = l ^ (i ^ n)
        return l

# @lc code=end

