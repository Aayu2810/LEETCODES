from typing import List
from bisect import bisect_right
class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()  
        max_elements_to_keep = 0
        for i, min_value in enumerate(nums):
            right_bound = bisect_right(nums, k * min_value)
            max_elements_to_keep = max(max_elements_to_keep, right_bound - i)
        return len(nums) - max_elements_to_keep