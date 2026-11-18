class Solution:
    def binary_search(self, nums: list[int], target: int, start: int, end: int) -> int:
        if start > end:
            return -1

        mid = start + (end - start) // 2
        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            return self.binary_search(nums, target, mid + 1, end)
        else:
            return self.binary_search(nums, target, start, mid - 1)


    def search(self, nums: list[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        return self.binary_search(nums, target, start, end)