/*
 * @lc app=leetcode id=83 lang=cpp
 *
 * [83] Remove Duplicates from Sorted List
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if(!head) return head;
        ListNode* ptr = head->next;
        ListNode* prev = head;
        while(ptr != nullptr){
            if(ptr->val == prev->val){
                ptr = ptr->next;
                prev->next = ptr;
            }
            else{
                ptr = ptr->next;
                prev = prev->next;
            }
        }
        return head;
    }
};

// @lc code=end

