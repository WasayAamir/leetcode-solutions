class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #initalize left pointer
        l = 0
        #get the length of the inter array
        n = len(nums)

        for r in range(n):
            if nums[r] != 0:
                nums[l],nums[r] = nums[r],nums[l]
                l = l + 1
        return nums