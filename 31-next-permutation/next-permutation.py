class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        pivot = None

        # Start at n - 2 to prevent IndexError when checking nums[i + 1]
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                pivot = i
                break

        if pivot is None:
            # Reversing is O(N) time, which is faster than sort() which is O(N log N)
            nums.reverse()
            return  # CRITICAL: Stop execution here

        for i in range(n - 1, pivot, -1):
            if nums[i] > nums[pivot]:
                nums[i], nums[pivot] = nums[pivot], nums[i]
                break
        
        # Reverse the suffix using your exact two-pointer logic
        i = pivot + 1
        j = n - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1