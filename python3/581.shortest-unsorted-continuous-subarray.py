#
# @lc app=leetcode id=581 lang=python3
#
# [581] Shortest Unsorted Continuous Subarray
#

# @lc code=start
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        l_max = []
        r_min = []
        max_temp = -float('inf')
        for n in range(len(nums)):
            max_temp = max(nums[n], max_temp)
            l_max.append(max_temp)
        min_temp = float('inf')
        for n in reversed(range(len(nums))):
            min_temp = min(nums[n], min_temp)
            r_min.append(min_temp)
        r_min = r_min[::-1]
        
        l, r = -1, -1
        for n in range(len(nums)):
            if nums[n] != r_min[n]:
                l = n
                break
        for n in reversed(range(len(nums))):
            if nums[n] != l_max[n]:
                r = n
                break
        if l == r: return 0
        return r - l + 1
                
# @lc code=end

