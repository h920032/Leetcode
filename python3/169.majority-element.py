#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
# hash set
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s = {}
        max_n = nums[0]
        for i in nums:
            if i not in s:
                s[i] = 1
            else:
                s[i] += 1
            if s[i] >= s[max_n]: max_n = i
        return max_n

# Boyer-Moore Voting Algorithm
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        c = -1
        for i in nums:
            if count == 0: c = i
            if i == c:
                count += 1
            else:
                count -= 1
        return c
        
# @lc code=end

