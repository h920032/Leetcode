#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = [0] * 3
        for i in nums:
            count[i] += 1
        current = 0
        s = 0
        while s < len(nums) and current <= 2:
            if count[current] == 0:
                current += 1
            else:
                nums[s] = current
                count[current] -= 1
                s += 1
        
# one pass solution
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l = len(nums)
        if l == 1: return None
        right = l - 1
        left = 0
        current = 0
        
        def swap(a, b):
            temp = nums[a]
            nums[a] = nums[b]
            nums[b] = temp
        
        while current <= right:
            if nums[current] == 0 and current != left:
                swap(current, left)
                while nums[left] == 0 and left < right:
                    left += 1
                while nums[right] == 2  and left < right:
                    right -= 1
                while current < left:
                    current += 1
            elif nums[current] == 2 and current != right:
                swap(current, right)
                while nums[left] == 0 and left < right:
                    left += 1
                while nums[right] == 2 and left < right:
                    right -= 1
                while current < left:
                    current += 1
            else:
                current += 1

# @lc code=end

