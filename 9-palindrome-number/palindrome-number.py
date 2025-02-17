class Solution:
    def isPalindrome(self, x: int) -> bool:
        originalx = x
        numReversed = 0

        while x > 0:
            lastDigit = x % 10
            numReversed = numReversed * 10 + lastDigit
            x = x // 10 #12.1
        if numReversed == originalx:
                return True
        else:
            return False