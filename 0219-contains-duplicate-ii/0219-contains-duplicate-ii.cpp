class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        std::unordered_map<int, int> num_to_index; 
        for (int i = 0; i < nums.size(); ++i) {
            int current_num = nums[i];
            if (num_to_index.count(current_num)) {
                if (std::abs(i - num_to_index[current_num]) <= k) {
                    return true;
                }
            }
            num_to_index[current_num] = i;
        }
        return false;
    }
};