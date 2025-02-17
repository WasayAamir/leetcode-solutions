class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()               #sort the numbers from lowest to greatest
        n = len(nums)             # get the length of the array
        answer = []               #make a empty array that you will add the solutions to
            
        for i in range(n):       #iterate over the array
            if nums[i] > 0:      #if your first number the i is greater than 0 break because all the other will have to be as well meaning all positives and u cant get = 0
                break
            elif i > 0 and nums[i] == nums[i-1]:  #if first number greater than 0 and the next number ur on is the same as previous just keep going
                continue 
            
            l = i + 1    #left pointer right after i
            r = n-1      #right pointer at the end of the array last number

            while l < r:        #while left is less than right
                summ = nums[i] + nums[l] + nums[r]   # sum is adding them all up
                if summ == 0:   #if we do get 0 then add the three pointer values to the answer empty array we made
                    answer.append([nums[i], nums[l], nums[r]])
                    l = l + 1 #after finding solution, grow left by one 
                    r = r - 1 #decrease right by 1
                    while l < r and nums[l] == nums[l-1]: #make sure l still less than r and a diff number than previous
                        l = l + 1
                    while l < r and nums[r] == nums[r+1]: #same thing here make sure right a different number
                        r = r - 1
                elif summ < 0:  #if the sum is too small like -1, increase left pointer by 1 cause too small
                    l = l + 1
                else:  #if too big like 1, decrease the right pointer by 1
                    r = r - 1
        return answer
