class Solution(object):
    def merge(self, nums1, m, nums2, n):
        
        #get the last index of nums1
        last = m + n - 1

        #merge them in reverse order
        while m > 0 and n > 0:                    #still elements in both arrays
            if nums1[m - 1] > nums2[n - 1]:     #if the values in nums1 are greater than values in nums2 that we compare
                nums1[last] = nums1[m-1]        #then put nums one biggest value at the back or end of nums1
                m = m - 1                       #keep decrementing the pointer in nums1 by 1 
            else:                               #else put nums 2 biggest value at the back or end of nums1
                nums1[last] = nums2[n-1]
                n = n - 1                       #keep decrementing the pointer in nums2 by 1 
            last = last - 1                      #regardless decrement last pointer by 1
        while n > 0:                              #making sure there are still elements in nums2
            nums1[last] = nums2[n-1]               #if there are add them in wtv space left in nums1
            n,last = n - 1, last - 1                #decrement last by one and nums2 pointer by 1