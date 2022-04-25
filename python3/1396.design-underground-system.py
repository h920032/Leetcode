#
# @lc app=leetcode id=1396 lang=python3
#
# [1396] Design Underground System
#

# @lc code=start
class UndergroundSystem:

    def __init__(self):
        self.d = {}
        self.check_in = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        stat, t_n = self.check_in[id]
        self.check_in.pop(id)
        if (stat, stationName) in self.d:
            s, count = self.d[(stat, stationName)]
            self.d[(stat, stationName)] = (s + t - t_n, count + 1)
        else:
            self.d[(stat, stationName)] = (t - t_n, 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        s, count = self.d[(startStation, endStation)]
        return s / count        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
# @lc code=end

