#
# @lc app=leetcode id=1249 lang=python3
#
# [1249] Minimum Remove to Make Valid Parentheses
#

# @lc code=start
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        right_out = ""
        l = len(s)
        for i in range(l):
            if s[i] == '(':
                stack.append(s[i])
                right_out += s[i]
            elif s[i] == ')':
                if len(stack) != 0 and stack[-1] == '(':
                    right_out += s[i]
                    stack.pop()
            else:
                right_out += s[i]
        
        stack = []
        left_out = ""
        for i in range(len(right_out) - 1, -1, -1):
            if right_out[i] == ')':
                stack.append(right_out[i])
                left_out = right_out[i] + left_out
            elif right_out[i] == '(':
                if len(stack) != 0 and stack[-1] == ')':
                    left_out = right_out[i] + left_out
                    stack.pop()
            else:
                left_out = right_out[i] + left_out
        return left_out
                
# @lc code=end

