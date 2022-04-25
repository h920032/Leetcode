#
# @lc app=leetcode id=2034 lang=python3
#
# [2034] Stock Price Fluctuation 
#

# @lc code=start
class StockPrice:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        self.org = {}
        self.highest_time = 0

    def update(self, timestamp: int, price: int) -> None:
        heappush(self.max_heap, (-price, timestamp))
        heappush(self.min_heap, (price, timestamp))
        self.highest_time = max(self.highest_time, timestamp)
        self.org[timestamp] = price

    def current(self) -> int:
        return self.org[self.highest_time]

    def maximum(self) -> int:
        p, t = self.max_heap[0]
        while True:
            if self.org[t] == -p: break
            heappop(self.max_heap)
            p, t = self.max_heap[0]
        return -p

    def minimum(self) -> int:
        p, t = self.min_heap[0]
        while True:
            if self.org[t] == p: break
            heappop(self.min_heap)
            p, t = self.min_heap[0]
        return p

# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
# @lc code=end

