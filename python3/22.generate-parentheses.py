#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        @cache
        def dp(n):
            if n == 0: return [""]
            out = []
            for i in range(n):
                out += ["({}){}".format(a,b) for a in dp(i) for b in dp(n - 1 - i)]
            return out
        return dp(n)


# @lc code=end

