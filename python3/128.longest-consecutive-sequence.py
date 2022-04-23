#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        max_count = 0
        for n in nums:
            if n in s:
                temp = n + 1
                count = 1
                while temp in s:
                    s.remove(temp)
                    temp += 1
                    count += 1
                temp = n - 1
                while temp in s:
                    s.remove(temp)
                    temp -= 1
                    count += 1
                max_count = max(count, max_count)
        return max_count

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_dict = defaultdict(int)
        maxi = 0
        for num in nums:
            if num not in my_dict.keys():
                prev_ = my_dict.get(num-1, 0)
                next_ = my_dict.get(num+1, 0)
                my_dict[num] += prev_ + next_ + 1
                my_dict[num-prev_] = my_dict[num]
                my_dict[num+next_] = my_dict[num]
                maxi = max(maxi, my_dict[num])
        return maxi

# @lc code=end

