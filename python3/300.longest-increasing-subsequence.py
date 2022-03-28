#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        @cache
        def dp(n):
            max_len = 1
            for i in range(n):
                if nums[n] > nums[i]:
                    max_len = max(max_len, dp(i) + 1)
            return max_len
        return max([dp(i) for i in range(1, len(nums))])    
            
# @lc code=end

