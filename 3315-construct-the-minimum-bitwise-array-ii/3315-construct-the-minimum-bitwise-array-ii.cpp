class Solution {
 public:
  vector<int> minBitwiseArray(vector<int>& nums) {
    vector<int> ans;

    for (const int num : nums)
      ans.push_back(num == 2 ? -1 : num - getLeadingOneOfLastGroupOfOnes(num));

    return ans;
  }

 private:
  int getLeadingOneOfLastGroupOfOnes(int num) {
    int leadingOne = 1;
    while ((num & leadingOne) > 0)
      leadingOne <<= 1;
    return leadingOne >> 1;
  }
};