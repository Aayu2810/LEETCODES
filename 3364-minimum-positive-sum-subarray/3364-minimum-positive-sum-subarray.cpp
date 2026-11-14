class Solution {
public:
    int minimumSumSubarray(vector<int>& nums, int l, int r) {
        int n = nums.size(), best = INT_MAX;
        vector<int> pre(n + 1);
        partial_sum(nums.begin(), nums.end(), pre.begin() + 1);
        for (int k = l; k <= r; ++k)
            for (int i = 0; i + k <= n; ++i) {
                int s = pre[i + k] - pre[i];
                if (s > 0) best = min(best, s);
            }
        return best == INT_MAX ? -1 : best;
    }
};