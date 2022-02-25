#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        l = len(nums)
        def swap(nums, start):
            for i in range((l-start)//2):
                temp = nums[start + i]
                nums[start + i] = nums[l - 1 - i]
                nums[l - 1 - i] = temp
        
        for i in range(l - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                min_sat = 101
                min_index = -1
                for j in range(i + 1, l):
                    if nums[j] > nums[i] and min_sat >= nums[j]:
                        min_sat = nums[j]
                        min_index = j
                temp = nums[i]
                nums[i] = nums[min_index]
                nums[min_index] = temp
                swap(nums, i + 1)
                return None
        swap(nums, 0)
        return None
        '''
        def rec(nums, start):
            max_index = start
            for j in range(start, l):
                if nums[j] >= nums[max_index]:
                    max_index = j
            if max_index == -1: return False
            if max_index == start:
                if start < l:
                    return rec(nums, start + 1)
                return False
            if max_index == l - 1:
                for i in range(max_index, -1, -1):
                    if nums[i] < nums[max_index]:
                        temp = nums[i+1]
                        nums[i+1] = nums[i]
                        nums[i] = temp
                        return True
                return False
            r = rec(nums, max_index)
            if not r:
                t = max_index
                while nums[t] == nums[max_index]:
                    t -= 1
                sat_min = 101
                min_index = -1
                for i in range(max_index, l):
                    if nums[i] > nums[t] and nums[i] < sat_min:
                        sat_min = nums[i]
                        min_index = i
                temp = nums[t]
                nums[t] = nums[min_index]
                nums[min_index] = temp
                swap(nums, t + 1)
                return True
            return r
            '''
            


        
# @lc code=end

