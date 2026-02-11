class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nonz = []

        for i in nums:
            if i != 0:
                nonz.append(i)

        j = 0
        
        for i in range(len(nums)):
            if j < len(nonz):
                nums[i] = nonz[j]
                j += 1
            else:
                nums[i] = 0

        return nums