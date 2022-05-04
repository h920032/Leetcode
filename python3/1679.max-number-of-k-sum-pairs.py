#
# @lc app=leetcode id=1679 lang=python3
#
# [1679] Max Number of K-Sum Pairs
#

# @lc code=start
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d = {}
        for n in nums:
            if n in d: d[n] += 1
            else: d[n] = 1
        
        count = 0
        
        for i in d:
            if k-i in d:
                if i != k-i:
                    target = min(d[i], d[k-i])
                    count += target
                    d[i] -= target
                    d[k-i] -= target
                else:
                    target = d[i] // 2
                    count += target
                    d[i] -= target
        return count
                
# @lc code=end

