class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1

        # Array having only one element.
        if end == 0:
            return nums[0]
        while start <= end:
            mid = start + (end - start) // 2
            # Element at 1st index.
            if mid == 0 and nums[0] != nums[1]:
                return nums[mid]
            # Element at last index.
            if mid == end and nums[end] != nums[end - 1]:
                return nums[mid]

            # Mid condition.....
            if nums[mid - 1] != nums[mid] != nums[mid + 1]:
                return nums[mid]

            if mid % 2 == 0:  # Even...........
                if nums[mid - 1] == nums[mid]:   # Left side.
                    end = mid - 1
                else:    # Right side..........
                    start = mid + 1
            else:       # Odd........................
                if nums[mid - 1] == nums[mid]:  # Right side..........
                    start = mid + 1
                else:    # Left side............
                    end = mid - 1