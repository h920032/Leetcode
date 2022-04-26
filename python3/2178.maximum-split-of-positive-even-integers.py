#
# @lc app=leetcode id=2178 lang=python3
#
# [2178] Maximum Split of Positive Even Integers
#

# @lc code=start
class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 == 1: return []
        finalSum = finalSum // 2
        n = 0
        out = []
        while finalSum - n > 0:
            n += 1
            finalSum -= n
            out.append(n)
        i = len(out) - 1
        while finalSum > 0:
            out[i] += 1
            i -= 1
            finalSum -= 1
        for i in range(len(out)):
            out[i] *= 2
        return out

class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 == 1: return []
        finalSum = finalSum // 2
        n = 0
        out = []
        while finalSum - n > 0:
            n += 1
            finalSum -= n
            out.append(2 * n)
        out[-1] += finalSum * 2
        return out        
# @lc code=end

