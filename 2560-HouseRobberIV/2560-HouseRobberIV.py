class Solution(object):
    def minCapability(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def canRobWithCapability(cap):
            count, i = 0, 0
            while i < len(nums):
                if nums[i] <= cap:
                    count += 1
                    i += 1  # Skip the next house (since adjacent houses cannot be robbed)
                i += 1  # Move to the next house
            return count >= k

        left, right = min(nums), max(nums)
        while left < right:
            mid = (left + right) // 2
            if canRobWithCapability(mid):
                right = mid  # Try lowering the capability
            else:
                left = mid + 1  # Increase capability if k houses can't be robbed

        return left
