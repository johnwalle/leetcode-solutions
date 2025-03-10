class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        max_water = 0

        while left < right:
            # Calculate the area
            min_height = min(height[left], height[right])
            width = right - left
            area = min_height * width
            max_water = max(max_water, area)

            # Move the pointer pointing to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water
