class Solution:
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        max_length = 0
        for start in range(len(nums)):
            curr_length = 1
            for pos in range(start + 1, len(nums)):
                if nums[pos] > nums[pos - 1]:
                    curr_length += 1
                else:
                    break
            max_length = max(max_length, curr_length)
        for start in range(len(nums)):
            curr_length = 1
            for pos in range(start + 1, len(nums)):
                if nums[pos] < nums[pos - 1]:
                    curr_length += 1
                else:
                    break
            max_length = max(max_length, curr_length)
        return max_length