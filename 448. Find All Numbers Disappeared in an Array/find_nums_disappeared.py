class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums) #find length of nums array 
        store = set(range(1, n + 1)) # creates store and put set on it in between range [1,n+1] inclusive       


        nums.sort()   #sort input array to group duplicates together
        for num in nums:    #checks over the nums in nums list
            store.discard(num)  #goes back to store which is in a set and says, if that number is in nums array remove it from store    
        
        return list(store) #after the removal from checking nums and store, whatever is left in store we return