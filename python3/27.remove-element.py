#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = len(nums)
        if l == 0:
            return 0
        out = []
        s = 0
        for i in range(l):
            p = nums.pop(0)
            if p != val:
                s += 1
                out.append(p)
        nums += out
        return s
# @lc code=end

