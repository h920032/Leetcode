#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                l = [i] + l
            else:
                if len(l) != 0:
                    a = l.pop(0)
                    if i == ')' and a != '(': return False
                    elif i == '}' and a != '{': return False
                    elif i == ']' and a != '[': return False
                else:
                    return False
        if len(l) == 0:
            return True
        else:
            return False
        
# @lc code=end

