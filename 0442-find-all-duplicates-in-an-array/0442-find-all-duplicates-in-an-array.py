class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []              #empty list 

        for n in nums:     #iterate over the input array    
            n = abs(n)    #get abs value of all so it doesn't interfere with our indexing
            if nums[n-1] < 0:  #if the index you go to is alrdy negaive its been visited meaning duplicated
                res.append(n)      #add it to the res list
            nums[n-1] = -nums[n-1]  # for every iteration minus the value by 1 (4-1=3) go to index 3 make ITS value negative, this the procedure of marking it visited
        return res  #return the appended list
