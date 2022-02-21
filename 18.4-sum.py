#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#

# @lc code=start
class Solution:
    def fourSum(self, nums, target: int):
        l = len(nums)
        nums = sorted(nums)
        r = []
        for i in range(l-3):
            for j in range(i+1, l-2):
                left = j + 1
                right = l - 1
                while left < right:
                    qul = [nums[i], nums[j], nums[left], nums[right]]
                    temp = sum(qul)
                    if temp > target:
                        right -= 1
                    elif temp < target:
                        left += 1
                    else:
                        if qul not in r:
                            r.append(qul)
                        left += 1
        return r
# @lc code=end

