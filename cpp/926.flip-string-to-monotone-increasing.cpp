/*
 * @lc app=leetcode id=926 lang=cpp
 *
 * [926] Flip String to Monotone Increasing
 */

// @lc code=start
class Solution {
public:
    int minFlipsMonoIncr(string s) {
        s = "0" + s;
        int sum = 0;
        for(char c: s) if(c == '1') sum++;
        int count = 0;
        int min_times = s.length(); 
        for(int i = 0; i < s.length(); i++) {
            if(s[i] == '1') count++;
            int times = count + (s.length() - i - 1) -  (sum - count);
            min_times = min(times, min_times);
        }
        return min_times;
    }
};

// @lc code=end

