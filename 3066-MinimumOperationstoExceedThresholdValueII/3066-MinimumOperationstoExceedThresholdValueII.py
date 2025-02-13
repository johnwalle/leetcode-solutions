import heapq

class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Convert the list to a min-heap
        heapq.heapify(nums)
        operations = 0
        
        # Continue until the smallest element is >= k
        while nums[0] < k:
            # Pop the two smallest elements
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            
            # Calculate the new element to be added
            new_value = min(x, y) * 2 + max(x, y)
            
            # Add the new value back to the heap
            heapq.heappush(nums, new_value)
            
            # Increment the operation count
            operations += 1
        
        return operations
