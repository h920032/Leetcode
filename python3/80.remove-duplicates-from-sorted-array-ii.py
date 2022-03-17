#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = len(nums)
        current = nums[0]
        count = 1
        all_count = 1
        for i in range(1, l):
            if current == nums[i]:
                count += 1
                if count > 2:
                    nums[i] = None
                else:
                    all_count += 1
            else:
                count = 1
                current = nums[i]
                all_count += 1
        last_space = 100000
        for i in range(l):
            if nums[i] == None:
                last_space = min(last_space, i)
            elif i > last_space:
                nums[last_space] = nums[i]
                nums[i] = None
                last_space += 1
        return all_count

# short
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = len(nums)
        current = nums[0]
        count = 1
        all_count = 1
        last_space = 100000
        for i in range(1, l):
            if current == nums[i]:
                count += 1
                if count > 2:
                    nums[i] = None
                    last_space = min(last_space, i)
                    continue
            else:
                count = 1
                current = nums[i]
            all_count += 1
            if i > last_space:
                nums[last_space] = nums[i]
                nums[i] = None
                last_space += 1
        return all_count

# @lc code=end

