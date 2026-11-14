class Solution:
    def minimumSumSubarray(self, nums: list[int], l: int, r: int) -> int:
        pre = [0, *accumulate(nums)]  
        sums = (pre[i + k] - pre[i] for k in range(l, r + 1) for i in range(len(pre) - k))   
        return min((s for s in sums if s > 0), default=-1)