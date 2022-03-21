#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        out = [[-1] * n for i in range(n)]
        row = True
        d = 1
        c = 0
        current_r = 0
        current_c = 0
        count = 1
        while c != n:
            out[current_r][current_c] = count
            if row:
                if (d == 1 and current_c < n - c - 1) or (d != 1 and current_c > c):
                    current_c += d
                    count += 1
                else:
                    row = not row
                    if d == -1: c += 1
            else:
                if (d == 1 and current_r < n - c - 1) or (d != 1 and current_r > c):
                    current_r += d
                    count += 1
                else:
                    row = not row
                    d = -d
        return out
       
# strange solution

class Solution:
    def generateMatrix(self, n):
        A, lo = [], n*n+1
        while lo > 1:
            lo, hi = lo - len(A), lo
            A = [range(lo, hi)] + list(zip(*A[::-1]))
            print(A)
        return A

# @lc code=end

