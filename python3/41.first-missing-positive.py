#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        l = len(nums)
        def find(n):
            if nums[n - 1] <= 0 or nums[n - 1] > len(nums) or nums[n - 1] == n: nums[n - 1] = n
            else:
                temp = nums[n - 1]
                nums[n - 1] = n
                find(temp)
        for i in range(l):
            if nums[i] <= 0 or nums[i] > len(nums): nums[i] = 0
            elif nums[i] - 1 != i:
                temp = nums[i]
                nums[i] = 0
                find(temp)
        for i in range(l):
            if nums[i] == 0: return i + 1
        return l + 1
# brillent solution
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.append(0)
        l = len(nums)
        for i in range(l):
            if nums[i] < 0 or nums[i] >= l: nums[i] = 0
        for i in range(l):
            nums[nums[i] % l] += l
        for i in range(1,l):
            if nums[i] // l == 0: return i
        return l

# @lc code=end

