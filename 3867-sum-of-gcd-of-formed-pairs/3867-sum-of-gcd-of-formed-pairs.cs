public class Solution {
    public long GcdSum(int[] nums) {
        int n = nums.Length;

        int[] mx = new int[n];
        int prefixMax = int.MinValue;

        for (int i = 0; i < n; ++i) {
            prefixMax = Math.Max(prefixMax, nums[i]);
            mx[i] = prefixMax;
        }

        int[] prefixGcd = new int[n];
        for (int i = 0; i < n; ++i) {
            prefixGcd[i] = GCD(nums[i], mx[i]);
        }

        Array.Sort(prefixGcd);

        long ans = 0;
        int left = 0, right = n - 1;
        while (left < right) {
            ans += GCD(prefixGcd[left], prefixGcd[right]);
            ++left;
            --right;
        }

        return ans;
    }

    public int GCD(int num1, int num2) {
        while (num2 != 0) {
            int temp = num1;
            num1 = num2;
            num2 = temp % num2;
        }
        return num1;
    }
}