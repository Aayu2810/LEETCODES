int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int findGCD(int* nums, int numsSize) {
    int mx = nums[0];
    int mn = nums[0];
    for (int i = 1; i < numsSize; i++) {
        if (nums[i] > mx) {
            mx = nums[i];
        }
        if (nums[i] < mn) {
            mn = nums[i];
        }
    }
    return gcd(mx, mn);
}