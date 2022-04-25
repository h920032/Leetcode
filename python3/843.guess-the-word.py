#
# @lc app=leetcode id=843 lang=python3
#
# [843] Guess the Word
#

# @lc code=start
# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        arr = [{} for _ in range(6)]
        
        for w in wordlist:
            for c in range(6):
                if w[c] in arr[c]: arr[c][w[c]] += 1
                else: arr[c][w[c]] = 1
        distinct = []
        for i in range(len(wordlist)):
            count = 0
            for c in range(6):
                count += arr[c][wordlist[i][c]]
            heappush(distinct, (-count, wordlist[i]))
        
        candidate = []
        for _ in range(10):
            match = False
            c, w = 0,''
            while not match and distinct:
                c, w = heappop(distinct)
                c_match = True
                for c_w, c_i in candidate:
                    if c_i == 0:
                        for i in range(6):
                            if c_w[i] == w[i]:
                                c_match = False
                                break
                    else:
                        count = 0
                        for i in range(6):
                            if c_w[i] == w[i]: count += 1
                        if count < c_i or count == 6: c_match = False
                match = c_match
            i = master.guess(w)
            candidate.append((w, i))
                    
# @lc code=end

