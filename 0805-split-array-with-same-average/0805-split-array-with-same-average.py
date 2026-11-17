class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        nums.sort(reverse=True)
        n = len(nums)

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        
        def can_make(k: int, target_sum: int, first: int) -> bool:
            if k == 0:
                return target_sum == 0
            if target_sum < prefix[n] - prefix[n - k]:
                return False
            
            for i in range(first, n - k + 1):
                if target_sum > prefix[i + k] - prefix[i]:
                    return False
                if can_make(k - 1, target_sum - nums[i], i + 1):
                    return True
            return False

        for k in range(1, n // 2 + 1):
            if (prefix[n] * k) % n == 0:
                if can_make(k, (prefix[n] * k) // n, 0):
                    return True
                    
        return False