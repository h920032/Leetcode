#
# @lc app=leetcode id=60 lang=python3
#
# [60] Permutation Sequence
#

# @lc code=start
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        if k == factorial(n): return ''.join([str(i + 1) for i in reversed(range(n))])
        order = []
        temp = n
        k -= 1
        while k > 0 and temp > 0:
            temp -= 1
            r = k // factorial(temp)
            k = k % factorial(temp)
            order.append(r)
        arr = [str(i + 1) for i in range(n)]
        out = ''
        for i in order:
            out += arr[i]
            arr = arr[:i] + arr[i + 1:]
        out += ''.join(arr)
        return out

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        if k == factorial(n): return ''.join([str(i + 1) for i in reversed(range(n))])
        order = []
        k -= 1
        for temp in range(n - 1, -1, -1):
            r = k // factorial(temp)
            k -= r * factorial(temp)
            order.append(r)
        arr = [str(i + 1) for i in range(n)]
        out = ''
        for i in order:
            out += arr[i]
            arr = arr[:i] + arr[i + 1:]
        out += ''.join(arr)
        return out

# @lc code=end

