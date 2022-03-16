#
# @lc app=leetcode id=946 lang=python3
#
# [946] Validate Stack Sequences
#

# @lc code=start
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        l_push = len(pushed)
        l_pop = len(popped)
        i_push = 0
        i_pop = 0
        while i_pop < l_pop:
            if len(stack) != 0 and stack[-1] == popped[i_pop]:
                stack.pop()
                i_pop += 1
            elif i_push < l_push:
                stack.append(pushed[i_push])
                i_push += 1
            else: return False
        return True
                        
# @lc code=end

