class Solution {
public:
    int countTrapezoids(vector<vector<int>>& points) {
    
        const int mod = 1e9 + 7;
        unordered_map<int, int> freq;
        for (const auto& p : points) {
            freq[p[1]]++;
        }

        long long total = 0;
        long long sum_of_squares = 0;

        for (const auto& f : freq) {
            if (f.second <= 1) {
                continue;
            }

            long long pairs_at_height = (long long)f.second * (f.second - 1) / 2;
            
            total = (total + pairs_at_height) % mod;
            
            sum_of_squares = (sum_of_squares + (pairs_at_height * pairs_at_height) % mod) % mod;
        }
        long long result = (total * total) % mod;
        result = (result - sum_of_squares + mod) % mod; 
        long long invTwo = 500000004;
        result = (result * invTwo) % mod;

        return (int)result;
    }
};
