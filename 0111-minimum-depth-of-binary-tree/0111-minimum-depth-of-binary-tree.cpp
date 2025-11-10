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
    int minDepth(TreeNode* root) {
        if (root == nullptr) {
            return 0; 
        }
        std::queue<std::pair<TreeNode*, int>> q;
        q.push({root, 1}); 
        while (!q.empty()) {
            TreeNode* current_node = q.front().first;
            int current_depth = q.front().second;
            q.pop();
            if (current_node->left == nullptr && current_node->right == nullptr) {
                return current_depth;
            }
            if (current_node->left != nullptr) {
                q.push({current_node->left, current_depth + 1});
            }
            if (current_node->right != nullptr) {
                q.push({current_node->right, current_depth + 1});
            }
        }
        return 0;
    }
};