class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # Step 1: Sort the array
        result = []
        
        for i in range(len(nums) - 2):
            # Skip duplicate elements for the 'i' position
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Two-pointer approach
            left, right = i + 1, len(nums) - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == 0:
                    # Found a valid triplet
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates for the 'left' pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicates for the 'right' pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # Move the pointers inward after finding a valid triplet
                    left += 1
                    right -= 1
                elif current_sum < 0:
                    left += 1  # We need a larger sum, so move the 'left' pointer
                else:
                    right -= 1  # We need a smaller sum, so move the 'right' pointer
        
        return result
