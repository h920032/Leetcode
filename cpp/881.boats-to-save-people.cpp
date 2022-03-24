/*
 * @lc app=leetcode id=881 lang=cpp
 *
 * [881] Boats to Save People
 */

// @lc code=start
class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        sort(people.begin(), people.end());
        int left = 0, right = people.size() - 1, count = 0;
        while(left <= right){
            if(left == right){
                left++;
            }
            else if(people[right] + people[left] > limit){
                right--;
            }
            else{
                right--;
                left++;
            }
            count++;
        }
        return count;
    }
};

// @lc code=end

