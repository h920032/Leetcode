#
# @lc app=leetcode id=68 lang=python3
#
# [68] Text Justification
#

# @lc code=start
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        len_count = 0
        w_count = -1
        output = []
        s = []
        for i in range(len(words)):
            if len_count + len(words[i]) + w_count + 1 <= maxWidth:
                len_count += len(words[i])
                w_count += 1
                s.append(words[i])
            else:
                r = maxWidth - len_count
                temp = ''
                if w_count < 2:
                    temp = s[0] + ' '*r
                    if w_count == 1:
                        temp += s[1]
                else:
                    k = r // w_count
                    q = r % w_count
                    for j in range(w_count + 1):
                        temp += s[j]
                        if j < w_count:
                            temp += ' '*k
                        if j < q:
                            temp += ' '
                output.append(temp)
                len_count = len(words[i])
                w_count = 0
                s = [words[i]]
        r = maxWidth - len_count - w_count
        temp = ''
        for i in range(len(s) - 1):
            temp += s[i] + ' '
        temp += s[-1] + ' '*r
        output.append(temp)
        return output
                
# @lc code=end

