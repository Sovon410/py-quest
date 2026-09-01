class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        # Helper function to find either the leftmost or rightmost boundary
        def findBound(is_first: bool) -> int:
            left, right = 0, len(nums) - 1
            bound = -1
            
            while left <= right:
                mid = left + (right - left) // 2
                
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    # Target found, but we don't stop searching.
                    bound = mid
                    if is_first:
                        # To find the first occurrence, discard the right half
                        right = mid - 1
                    else:
                        # To find the last occurrence, discard the left half
                        left = mid + 1
                        
            return bound

        # 1. Search for the extreme left boundary
        first = findBound(True)
        
        # If the target doesn't exist at all, skip the second search entirely
        if first == -1:
            return [-1, -1]
            
        # 2. Search for the extreme right boundary
        last = findBound(False)
        
        return [first, last]