class Solution:
    def missingInteger(self, nums: list[int]) -> int:
        prefix_len = 1
        num_set = set(nums)

        for prev, curr in zip(nums, nums[1:]):
            if curr == prev + 1:
                prefix_len += 1
            else:
                break

        total = (nums[prefix_len - 1] + nums[0]) * prefix_len // 2
        while total in num_set:
            total += 1

        return total