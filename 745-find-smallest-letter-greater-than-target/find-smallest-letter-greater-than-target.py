class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l = 0                                     #left at index 0
        r = len(letters) - 1                      #right at the last index  

        while l<=r:                                #while left is less than or equal right pointer
            m = (l+r) // 2                         #midpoint is left index + right index divide by 2 
            if letters[m] <= target:              # if the midpoint value is less than or equal to targ, keep updating left by 1
                l = m + 1
            else:                               #else if it greater decrease right by 1
                r = m - 1
        if l < len(letters):
            return letters[l]
        return letters[0]