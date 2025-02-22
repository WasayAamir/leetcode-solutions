class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        j = len(nums)

        for i in range(j):
            n = nums[i]** 2
            res.append(n)
            
        res.sort()
        return res
