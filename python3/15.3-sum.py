#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums):
        nums = sorted(nums)
        l = len(nums)
        d = {}
        for i in nums:
            if i in d: d[i]+=1
            else: d[i] = 1
        out = []
        for i in range(l):
            if i > 0 and nums[i] == nums[i - 1]: continue
            for j in range(i + 1, l):
                if j -1 != i and nums[j] == nums[j - 1]: continue
                t = 0 - (nums[i] + nums[j])
                if t in d and t >= nums[j]:
                    if d[t] >= 1+(nums[i]==t)+(nums[j]==t):
                        out.append([nums[i], nums[j], 0 - (nums[i] + nums[j])])
        return out
# @lc code=end

