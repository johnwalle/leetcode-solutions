class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # If the number is negative or ends with a zero but is not zero itself, it can't be a palindrome
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        
        # If the number is the same when read from left to right and right to left
        return x == reversed_half or x == reversed_half // 10
