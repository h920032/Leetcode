#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums:
            if n not in d: d[n] = 0
            else: d[n] += 1
        r = sorted(d.keys(), key=lambda x: d[x], reverse=True)
        return r[:k]

class Solution:
    def topKFrequent(self, nums, k):
        bucket = [[] for _ in range(len(nums) + 1)]
        Count = Counter(nums).items()  
        for num, freq in Count: 
            bucket[freq].append(num) 
        flat_list = list(chain(*bucket))
        return flat_list[::-1][:k]

# @lc code=end

