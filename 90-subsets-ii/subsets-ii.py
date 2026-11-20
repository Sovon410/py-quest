class Solution:
    def get_subset(self, nums: List[int], subset: List[int], idx: int, all_subset: List[List[int]]):
        if idx == len(nums):
            all_subset.append(subset.copy())
            return
        
        subset.append(nums[idx])
        self.get_subset(nums, subset, idx + 1, all_subset)

        subset.pop()

        next_idx = idx + 1
        while len(nums) > next_idx and nums[next_idx - 1] == nums[next_idx]:
            next_idx += 1

        self.get_subset(nums, subset, next_idx, all_subset)



    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()

        all_subset = []
        subset = []

        self.get_subset(nums, subset, 0, all_subset)
        return all_subset