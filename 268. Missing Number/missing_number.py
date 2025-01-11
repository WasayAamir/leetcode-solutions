class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums)    #getting the length of the nums array      

        nums.sort()          #sort the array so the indices and numbers in the list are the same 
        for i in range (n):    # loop through the input array
            if nums[i] != i:   # when you are checking, if the indices number doesnt equal the value
                return i       # return the number it doesnt equal to thats missing 
        return n               # edge case: incase no mismatch is found, just return the length of nums