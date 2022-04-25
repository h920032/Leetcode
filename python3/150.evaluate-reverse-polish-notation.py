#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c not in ['+','-','*','/']:
                stack.append(int(c))
            else:
                b = stack.pop()
                a = stack.pop()
                if c == '/':
                    if a/b != a//b:
                        if a/b > 0: stack.append(a//b)
                        else: stack.append(a//b + 1)
                    else: stack.append(a//b)
                elif c == '+':
                    stack.append(a+b)
                elif c == '-':
                    stack.append(a-b)
                elif c == '*':
                    stack.append(a*b)
        return stack[-1]
                
# @lc code=end

