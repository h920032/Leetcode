#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start

# One-pass Binary Search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = len(nums)
        left = 0
        right = l - 1
        while left < right:
            middle = (right - left + 1) // 2 + left -1
            if nums[middle] >= nums[left]:
                if target >= nums[left] and target <= nums[middle]:
                    right = middle
                else:
                    left = middle + 1
                continue
            if nums[right] >= nums[middle + 1]:
                if target >= nums[middle + 1] and target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle
                continue
        if target == nums[left]: return left
        return -1

# @lc code=end

