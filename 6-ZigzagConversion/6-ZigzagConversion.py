class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s
        
        rows = [""] * numRows
        curRow = 0
        direction = -1  # -1 means moving up, +1 means moving down

        for char in s:
            rows[curRow] += char
            # Change direction when reaching the top or bottom row
            if curRow == 0 or curRow == numRows - 1:
                direction *= -1
            curRow += direction

        return "".join(rows)
