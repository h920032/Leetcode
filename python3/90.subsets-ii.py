#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        nums = sorted(nums)
        for n in range(len(nums)):
            for i in range(len(result)):
                if result[i] + [nums[n]] not in result:
                    result.append(result[i] + [nums[n]])
        return result

# without hashing
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        nums = sorted(nums)
        r = [[]]
        new_r = []
        for n in range(len(nums)):
            if n != 0 and nums[n - 1] == nums[n]:
                r = new_r
            else:
                r = [] + result
            new_r = []
            for i in r:
                result.append(i + [nums[n]])
                new_r.append(i + [nums[n]])
        return result

# @lc code=end

