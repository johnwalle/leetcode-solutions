class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        total = 0
        prev_value = 0
        
        for char in reversed(s):  # Traverse from right to left
            value = roman_map[char]
            
            if value < prev_value:
                total -= value  # Subtract if a smaller value appears before a larger one
            else:
                total += value  # Otherwise, add normally
            
            prev_value = value  # Update previous value
        
        return total
