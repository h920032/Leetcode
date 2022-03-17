#
# @lc app=leetcode id=856 lang=python3
#
# [856] Score of Parentheses
#

# @lc code=start
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        out_score = 0
        l = len(s)
        for i in range(l):
            if s[i] == '(':
                stack.append(0)
            else:
                count = 2 * stack.pop()
                if count == 0: count = 1
                if len(stack) == 0:
                    out_score += count
                else:
                    stack[-1] += count
        return out_score

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for p in s:
            if p == '(':
                stack.append(0)
            else:
                count = max(2 * stack.pop(), 1)
                stack[-1] += count
        return stack.pop()
                    

# @lc code=end

