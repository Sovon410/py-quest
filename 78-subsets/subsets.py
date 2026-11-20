class Solution:
    def get_subset(self, array: List[int], subset: List[int], idx: int, all_subset: List[List[int]]):
        if idx == len(array):
            all_subset.append(subset.copy())
            return
        
        # Include......
        subset.append(array[idx])
        self.get_subset(array, subset, idx + 1, all_subset)

        subset.pop()
        # Exclude......
        self.get_subset(array, subset, idx + 1, all_subset)


    def subsets(self, nums: list[int]) -> list[list[int]]:
        all_subset = []
        subset = []

        self.get_subset(nums, subset, 0, all_subset)

        return all_subset
        