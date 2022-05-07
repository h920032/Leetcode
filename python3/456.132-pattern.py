#
# @lc app=leetcode id=456 lang=python3
#
# [456] 132 Pattern
#

# @lc code=start
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        min_l = []
        min_s = float('inf')
        stack = []
        for n in nums:
            min_s = min(n, min_s)
            min_l.append(min_s)
        for i in reversed(range(len(nums))):
            if nums[i] <= min_l[i]: continue
            while stack and stack[-1] <= min_l[i]:
                stack.pop()
            if stack and stack[-1] < nums[i]:
                return True
            stack.append(nums[i])
        return False
                
# @lc code=end

