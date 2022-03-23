#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        @cache
        def backtrack(i, j):
            if i == j:
                return 0
            s = 0
            for num in range(i, j):
                left = backtrack(i, num)
                right = backtrack(num + 1, j)
                if left == 0 and right == 0:
                    s += 1
                elif left != 0 and right != 0:
                    s += right * left
                else:
                    s += right + left
            return s
        return backtrack(0, n)  

#more simple
class Solution:
    def numTrees(self, n: int) -> int:
        @cache
        def count(l):
            if l <= 1: return 1
            s = 0
            for i in range(0, l):
                s += count(i - 0) * count(l - i - 1)
            return s
        return count(n)

# @lc code=end

