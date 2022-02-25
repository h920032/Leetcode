#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        if l == 0: return [-1,-1]
        if target > nums[-1] or target < nums[0]: return [-1,-1]
        left = 0
        right = l - 1
        t_right = -1
        t_left = -1
        while left < right:
            middle = (right - left + 1)// 2 + left
            if left + 1 == right:
                if nums[left] == target and nums[right] > target:
                    t_right = left
                else:
                    t_right = -1
                break
            if nums[middle] == target and nums[middle+1] > target:
                t_right = middle
                break
            if nums[middle] > target:
                right = middle
            elif nums[middle + 1] <= target:
                left = middle + 1
            else:
                t_right = -1
                break
        left = 0
        right = l - 1
        while left < right:
            middle = (right - left + 1)//2 + left
            if left + 1 == right:
                if nums[left] < target and nums[right] == target:
                    t_left = right
                else:
                    t_left = -1
                break
            if nums[middle] < target and nums[middle+1] == target:
                t_left = middle + 1
                break
            if nums[middle + 1] < target:
                left = middle + 1
            elif nums[middle] >= target:
                right = middle
            else:
                t_left = -1
                break
        if t_left == -1 and nums[0] == target:
            t_left = 0
        if t_right == -1 and nums[-1] == target:
            t_right = l-1
        return [t_left, t_right]


# @lc code=end

