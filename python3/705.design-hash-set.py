#
# @lc app=leetcode id=705 lang=python3
#
# [705] Design HashSet
#

# @lc code=start
class MyHashSet:
    def eval_hash(self, key):
        return ((key*1031237) & (1<<20) - 1)>>5
    
    def __init__(self):
        self.data = [[] for _ in range(2**15)]

    def add(self, key: int) -> None:
        if key not in self.data[self.eval_hash(key)]: self.data[self.eval_hash(key)].append(key)
        
        
    def remove(self, key: int) -> None:
        if key in self.data[self.eval_hash(key)]: self.data[self.eval_hash(key)].remove(key)

    def contains(self, key: int) -> bool:
        return key in self.data[self.eval_hash(key)]        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
# @lc code=end

