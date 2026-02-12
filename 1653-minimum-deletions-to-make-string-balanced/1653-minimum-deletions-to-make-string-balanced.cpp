class Solution {
 public:
  int minimumDeletions(string s) {
    int dp = 0;
    int countB = 0;
    for (const char c : s)
      if (c == 'a')
        dp = min(dp + 1, countB);
      else
        ++countB;
    return dp;
  }
};