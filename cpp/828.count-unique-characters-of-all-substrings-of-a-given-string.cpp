/*
 * @lc app=leetcode id=828 lang=cpp
 *
 * [828] Count Unique Characters of All Substrings of a Given String
 */

// @lc code=start
class Solution {
public:
    int uniqueLetterString(string s) {
        vector<vector<int>> index(26);
        for(int i = 0; i < 26; i++) index[i] = vector<int>{-1, -1};
        
        int res = 0;
        for(int i = 0; i < s.length(); i++){
            int c = s[i] - 'A';
            res += (i - index[c][1]) * (index[c][1] - index[c][0]);
            index[c][0] = index[c][1];
            index[c][1] = i;
        }
        
        for(int c = 0; c < 26; c++){
            res += (s.length() - index[c][1]) * (index[c][1] - index[c][0]);
        }
        
        return res;
    }
};

// @lc code=end

