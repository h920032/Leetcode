#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        max_count = 0
        count = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(-i)
            else:
                if len(stack) != 0:
                    new = (stack[-1], i)
                    flag = True
                    while count and flag:
                        flag = False
                        if len(count) > 0 and count[-1][1] + 1 == -stack[-1]:
                            new = (count[-1][0], i)
                            count.pop()
                            flag = True
                        elif len(count) > 0 and count[-1][0] + 1 ==  stack[-1] and count[-1][1] + 1 == i:
                            new = (stack[-1], i)
                            count.pop()
                            flag = True
                    count.append(new)
                    stack.pop()
        if not len(count): return 0
        return max([i[1] + i[0] + 1 for i in count])

# DP
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) == 0: return 0
        @cache
        def dp(i):
            if i < 1: return 0
            if s[i] == '(': return 0
            if s[i] == ')':
                if s[i - 1] == '(': return 2 + (dp(i-2) if i >=2 else 0)
                elif i - dp(i - 1) > 0 and s[i - dp(i - 1) - 1] == '(': return dp(i - 1) + 2 + (dp(i - dp(i - 1) -2) if i - dp(i - 1) >= 2 else 0)
            return 0
        return max(dp(i) for i in range(len(s)))

# @lc code=end

