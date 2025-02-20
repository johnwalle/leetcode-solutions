class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Create a set to store unique characters
        char_set = set()
        # Initialize the pointers and the maximum length variable
        left = 0
        max_length = 0
        
        # Iterate over the string with the right pointer
        for right in range(len(s)):
            # If the character at `right` is already in the set, move the left pointer
            while s[right] in char_set:
                char_set.remove(s[left])  # Remove the character at the `left` pointer
                left += 1  # Move `left` to the right
            
            # Add the current character to the set
            char_set.add(s[right])
            # Update the maximum length
            max_length = max(max_length, right - left + 1)
        
        return max_length
