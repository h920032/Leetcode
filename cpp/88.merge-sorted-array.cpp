/*
 * @lc app=leetcode id=88 lang=cpp
 *
 * [88] Merge Sorted Array
 */

// @lc code=start
class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        vector<int> out;
        int i = 0, j = 0;
        while(i < m or j < n){
            if(i < m and j < n){
                if(nums1[i] > nums2[j]){
                    out.push_back(nums2[j]);
                    j++;
                }
                else{
                    out.push_back(nums1[i]);
                    i++;
                }
            }
            else if(i < m){
                out.push_back(nums1[i]);
                i++;
            }
            else{
                out.push_back(nums2[j]);
                j++;
            }
        }
        for(int i = 0; i < m+n; i++){
            nums1[i] = out[i];
        }
    }
};

class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        vector<int> out;
        int i = 0, j = 0;
        while(i < m or j < n){
            if((i < m && j < n && nums1[i] > nums2[j]) || i == m){
                out.push_back(nums2[j]);
                j++;
            }
            else{
                out.push_back(nums1[i]);
                i++;
            }
        }
        for(int i = 0; i < m+n; i++){
            nums1[i] = out[i];
        }
    }
};

// @lc code=end

