#
# @lc app=leetcode id=1146 lang=python3
#
# [1146] Snapshot Array
#

# @lc code=start
class SnapshotArray:
    def __init__(self, length: int):
        self.base = {}
        self.diff = {}
        self.snap_shot = []
        self.snap_count = -1

    def set(self, index: int, val: int) -> None:
        if index not in self.base:
            self.base[index] = val
            self.diff[index] = 0
        else:
            self.diff[index] = val - self.base[index]

    def snap(self) -> int:
        self.snap_count += 1
        self.snap_shot.append(self.diff.copy())
        return self.snap_count

    def get(self, index: int, snap_id: int) -> int:
        if index in self.snap_shot[snap_id]:
            return self.snap_shot[snap_id][index] + self.base[index]
        else: return 0        

# binary search
class SnapshotArray:
    def __init__(self, length: int):
        self.arr = [[[0, 0]] for _ in range(length)]
        self.snap_count = 0

    def set(self, index: int, val: int) -> None:
        if self.arr[index][-1][0] == self.snap_count:
            self.arr[index][-1][1] = val
        else:
            self.arr[index].append([self.snap_count, val])

    def snap(self) -> int:
        self.snap_count += 1
        return self.snap_count - 1

    def get(self, index: int, snap_id: int) -> int:
        i = bisect.bisect(self.arr[index], [snap_id + 1]) - 1
        return self.arr[index][i][1]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
# @lc code=end

