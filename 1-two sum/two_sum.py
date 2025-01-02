class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)                                #checks the length of the list of numbers

        for i in range (n-1):   # loop with i which will be the first number in the pair, goes only goes till second last element in list
            for j in range (i+1, n):  #loop with j is second number in in pair, goes all the way to the end of list 
                if nums[i] + nums[j] == target:
                    return [i,j]
