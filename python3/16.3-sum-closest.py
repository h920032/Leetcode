#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        l = len(nums)
        nums = sorted(nums)
        s = sum(nums[:3])
        min_diff = abs(target-s)
        for i in range(0, l - 2):
            left = i + 1
            right = l - 1
            while left < right:
                temp = sum([nums[left], nums[right], nums[i]])
                if abs(target-temp) < min_diff:
                    min_diff = abs(target-temp)
                    s = temp
                if temp > target:
                    right -= 1
                elif temp < target:
                    left += 1
                else:
                    return target
        return s

# @lc code=end

