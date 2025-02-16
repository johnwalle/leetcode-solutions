class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MIN, INT_MAX = -2**31, 2**31 - 1  # Define 32-bit integer limits
        
        negative = x < 0  # Check if the number is negative
        x = abs(x)  # Work with absolute value
        
        reversed_x = 0
        while x != 0:
            digit = x % 10  # Get the last digit
            x //= 10  # Remove last digit
            
            # Check for overflow before multiplying by 10 and adding the digit
            if reversed_x > (INT_MAX - digit) // 10:
                return 0
            
            reversed_x = reversed_x * 10 + digit
        
        return -reversed_x if negative else reversed_x  # Restore sign if needed
