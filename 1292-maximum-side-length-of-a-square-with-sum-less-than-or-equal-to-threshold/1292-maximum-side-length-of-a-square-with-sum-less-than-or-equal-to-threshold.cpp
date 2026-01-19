class Solution {
public:
    int maxSideLength(vector<vector<int>>& mat, int threshold) {
         int rows = mat.size();
        int cols = mat[0].size();
        vector<vector<int>> prefixSum(rows + 1, vector<int>(cols + 1, 0));
        for (int i = 1; i <= rows; ++i) {
            for (int j = 1; j <= cols; ++j) {
                prefixSum[i][j] = prefixSum[i - 1][j] + prefixSum[i][j - 1]
                                 - prefixSum[i - 1][j - 1] + mat[i - 1][j - 1];
            }
        }
        auto feasible = [&](int k) -> bool {
            for (int i = 0; i <= rows - k; ++i) {
                for (int j = 0; j <= cols - k; ++j) {
                    int sum = prefixSum[i + k][j + k] - prefixSum[i][j + k]
                            - prefixSum[i + k][j] + prefixSum[i][j];
                    if (sum <= threshold) {
                        return true;
                    }
                }
            }
            return false;
        };
        int left = 1;
        int right = min(rows, cols) + 1;
        int firstTrueIndex = min(rows, cols) + 1; 
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (!feasible(mid)) { 
                firstTrueIndex = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return firstTrueIndex - 1;
    }
};