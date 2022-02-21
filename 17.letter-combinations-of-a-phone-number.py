#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {"2":"abc", "3":"def", "4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        def rec(digits):
            l = len(digits)
            r = []
            if l == 1: return [c for c in d[digits]]
            if l == 0: return r
            for i in d[digits[0]]:
                for j in rec(digits[1:]):
                    r.append(i + j)
            return r
        return rec(digits)

# @lc code=end

