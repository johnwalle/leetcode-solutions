class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Ensure that nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        
        while left <= right:
            partition1 = (left + right) // 2
            partition2 = (m + n + 1) // 2 - partition1
            
            # If partition1 is 0, there is no element on the left side of nums1
            # If partition1 is m, there is no element on the right side of nums1
            maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            minRight1 = float('inf') if partition1 == m else nums1[partition1]
            
            # If partition2 is 0, there is no element on the left side of nums2
            # If partition2 is n, there is no element on the right side of nums2
            maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            minRight2 = float('inf') if partition2 == n else nums2[partition2]
            
            # Check if we found the correct partition
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # If the total length is odd
                if (m + n) % 2 == 1:
                    return max(maxLeft1, maxLeft2)
                # If the total length is even
                return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
            elif maxLeft1 > minRight2:
                # Move partition1 to the left
                right = partition1 - 1
            else:
                # Move partition1 to the right
                left = partition1 + 1
        
        # If we reach here, the arrays are not sorted correctly or there's an issue with the input
        raise ValueError("Input arrays are not sorted.")
