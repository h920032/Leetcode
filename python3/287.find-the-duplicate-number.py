#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l = len(nums)
        for i in range(0, l):
            while nums[i] != i + 1:
                if nums[nums[i] - 1] != nums[i]:
                    nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
                else:
                    return nums[i]
                            
# @lc code=end

