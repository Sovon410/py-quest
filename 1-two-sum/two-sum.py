class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Stores seen numbers and their indices
        seen = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            # Check if the complement is already in the map
            if complement in seen:
                return [seen[complement], i]
            
            # Track the current number and its index
            seen[num] = i
