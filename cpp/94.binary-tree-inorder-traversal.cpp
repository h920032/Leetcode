/*
 * @lc app=leetcode id=94 lang=cpp
 *
 * [94] Binary Tree Inorder Traversal
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> out;
        if(!root) return out;
        triverse(root, out);
        return out;
    }
private:
    void triverse(TreeNode* node, vector<int> &out){
        if(node->left){
            triverse(node->left, out);
        }
        out.push_back(node->val);
        if(node->right){
            triverse(node->right, out);
        }
    }
};

//iteritave
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> out;
        vector<TreeNode*> stack;
        stack.push_back(root);
        if(!root) return out;
        while(stack.size()){
            TreeNode* target = stack.back();
            stack.pop_back();
            if(!target->left && !target->right){
                out.push_back(target->val);
            }
            if(target->right) stack.push_back(target->right);
            if(target->right or target->left) stack.push_back(target);
            if(target->left) stack.push_back(target->left);
            target->left = nullptr;
            target->right = nullptr;
        }
        return out;
    }
};

// @lc code=end

