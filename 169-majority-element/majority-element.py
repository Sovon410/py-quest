class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        nums.sort()  # Sorts in-place
        return nums[len(nums) // 2] 