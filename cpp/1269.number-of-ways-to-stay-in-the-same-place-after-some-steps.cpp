/*
 * @lc app=leetcode id=1269 lang=cpp
 *
 * [1269] Number of Ways to Stay in the Same Place After Some Steps
 */

// @lc code=start
class Solution {
public:
    vector<vector<string>> suggestedProducts(vector<string>& products, string searchWord) {
        vector<vector<string>> out;
        vector<int> count_list;
        sort(products.begin(), products.end());
        int l = searchWord.length();
        for(string s: products){
            int count = 0;
            for(int i = 0; i < l; i++){
                if(s.length() > i && s[i] == searchWord[i]) count++;
                else break;
            }
            count_list.push_back(count);
        }
        for(int i = 0; i < l; i++){
            vector<string> temp;
            int c = 0;
            for(int j = 0; j < count_list.size(); j++)
            {
                if(c < 3){
                    if(count_list[j] >= i + 1){
                        temp.push_back(products[j]);
                        c++;
                    }
                }
                else break;
            }
            out.push_back(temp);
        }
        return out;
    }
};

// @lc code=end

