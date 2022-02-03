#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l = len(digits)
        digits[l-1] += 1
        for i in range(l-1, 0, -1):
            if digits[i] == 10 and i != 0:
                digits[i-1] += 1
                digits[i] = 0
        if digits[0] == 10:
            digits[0] = 0
            return [1] + digits
        else:
            return digits
# @lc code=end

