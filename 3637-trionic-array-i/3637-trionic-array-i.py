class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        first_peak_index = 0
        while first_peak_index < n - 2 and nums[first_peak_index] < nums[first_peak_index + 1]:
            first_peak_index += 1
        if first_peak_index == 0:
            return False
        valley_index = first_peak_index
        while valley_index < n - 1 and nums[valley_index] > nums[valley_index + 1]:
            valley_index += 1
        if valley_index == first_peak_index or valley_index == n - 1:
            return False
        final_index = valley_index
        while final_index < n - 1 and nums[final_index] < nums[final_index + 1]:
            final_index += 1
        return final_index == n - 1