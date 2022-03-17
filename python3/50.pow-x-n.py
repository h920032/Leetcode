#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x < 0: return self.myPow(-x, n) if n%2 == 0 else -self.myPow(-x, n)
        if x == 1: return 1
        if n < 0: return self.myPow(1/x, -n)
        if n == 1: return x
        if n == 0: return 1
        i = 2
        new = x * x
        while i <= n:
            if new < 10**-5 : return 0
            if n % i == 0:
                break
            i += 1
            new *= x
        r = self.myPow(new, n//i)
        return r

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x < 0: return self.myPow(-x, n) if n%2 == 0 else -self.myPow(-x, n)
        if x == 1 or n == 0: return 1
        if n < 0: return self.myPow(1/x, -n)
        if n == 1: return x
        new = x * x
        if new < 10**-5 : return 0
        if n % 2 == 1:
            return x*self.myPow(new, (n - 1)//2)
        return self.myPow(new, n//2)

# @lc code=end

