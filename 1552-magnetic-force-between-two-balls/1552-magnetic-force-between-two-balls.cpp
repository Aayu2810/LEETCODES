class Solution {
public:
    bool canPlaceBalls(int x, vector<int> &position, int m) {
        int prevBallPos = position[0];
        int ballsPlaced = 1;
        for (int i = 1; i < position.size() && ballsPlaced < m; ++i) {
            int currPos = position[i];
            if (currPos - prevBallPos >= x) {
                ballsPlaced += 1;
                prevBallPos = currPos;
            }
        }
        return ballsPlaced == m;
    }
    int maxDistance(vector<int> &position, int m) {
        int answer = 0;
        int n = position.size();
        sort(position.begin(), position.end());
        int low = 1;
        int high = ceil(position[n - 1] / (m - 1.0));
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (canPlaceBalls(mid, position, m)) {
                answer = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return answer;
    }
};