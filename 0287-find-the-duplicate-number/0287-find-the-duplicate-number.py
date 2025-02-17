class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = slow = nums[0]
        
        #proves we have a cycle 
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            
            if fast == slow:
                break 
        #find where the cycle is by doing same speed for both
        fast = nums[0]
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]
        return slow
