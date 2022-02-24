#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        l = len(s)
        box = [[]]
        count = 0
        row = 0
        if numRows == 1: return s
        if numRows == 2:
            out = ""
            for i in range(0,l,2):
                out += s[i]
            for i in range(1,l,2):
                out += s[i]
            return out
        if numRows > 2:
            for c in s:
                if count == numRows - 1 - row %2:
                    if row %2 == 0:
                        box[row] += [c]
                    else:
                        box[row] = [c] + box[row]
                        box[row] = ["#"] + box[row] + ["#"]
                    box.append([])
                    row += 1
                    count = row %2
                else:
                    count += 1
                    if row %2 == 0:
                        box[row] += [c]
                    else:
                        box[row] = [c] + box[row]
            if row %2 == 0:
                for i in range(numRows - len(box[row])):
                    box[row].append("#")
            else:
                box[row].append("#")
                for i in range(numRows - len(box[row])):
                    box[row] = ["#"] + box[row]
        #print(box)
        out = ""
        for i in range(numRows):
            for j in box:
                if j[i] != "#":
                    out += j[i]
        return out
# @lc code=end

