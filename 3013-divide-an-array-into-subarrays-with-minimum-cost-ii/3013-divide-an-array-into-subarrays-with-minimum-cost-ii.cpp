class Solution {
public:
    long long minimumCost(vector<int>& nums, int k, int dist) {
        --k;
        multiset<int> leftSet(nums.begin() + 1, nums.begin() + dist + 2);
        multiset<int> rightSet;
        long long currentSum = accumulate(nums.begin(), nums.begin() + dist + 2, 0LL);
        while (leftSet.size() > k) {
            int largestInLeft = *leftSet.rbegin();
            leftSet.erase(leftSet.find(largestInLeft));
            currentSum -= largestInLeft;
            rightSet.insert(largestInLeft);
        }
        long long answer = currentSum;
        for (int i = dist + 2; i < nums.size(); ++i) {
            int elementToRemove = nums[i - dist - 1];
            auto iter = leftSet.find(elementToRemove);
            if (iter != leftSet.end()) {
                leftSet.erase(iter);
                currentSum -= elementToRemove;
            } else {
                rightSet.erase(rightSet.find(elementToRemove));
            }
          
            int newElement = nums[i];
            if (newElement < *leftSet.rbegin()) {
                leftSet.insert(newElement);
                currentSum += newElement;
            } else {
                rightSet.insert(newElement);
            }
          
            while (leftSet.size() == k - 1) {
                int smallestInRight = *rightSet.begin();
                rightSet.erase(rightSet.find(smallestInRight));
                leftSet.insert(smallestInRight);
                currentSum += smallestInRight;
            }
          
            while (leftSet.size() == k + 1) {
                int largestInLeft = *leftSet.rbegin();
                leftSet.erase(leftSet.find(largestInLeft));
                currentSum -= largestInLeft;
                rightSet.insert(largestInLeft);
            }
          
            answer = min(answer, currentSum);
        }
      
        return answer;
    }
};