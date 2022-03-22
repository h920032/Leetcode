#
# @lc app=leetcode id=81 lang=python3
#
# [81] Search in Rotated Sorted Array II
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1
        def b_search(start, end):
            if start == end:
                return nums[start] == target
            mid = start + (end - start) // 2
            if nums[mid] == target or nums[start] == target or nums[end] == target: return True
            if nums[start] > nums[mid]:
                if target > nums[mid] and target < nums[end]: start = mid + 1
                else: end = mid
                return b_search(start, end)
            elif nums[start] < nums[mid]:
                if target < nums[mid] and target > nums[start]: end = mid
                else: start = mid + 1
                return b_search(start, end)
            else:
                return b_search(start, end - 1) # worse case O(N)
        return b_search(left, right)

# @lc code=end

