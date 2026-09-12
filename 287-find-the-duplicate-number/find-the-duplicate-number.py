class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        seen = [0] * (len(nums) + 1)

        for num in nums:
            seen[num] += 1

        for num in range(1, len(nums) + 1):
            if seen[num] > 1:
                return num

        # seen = set()

        # for num in nums:
        #     if num in seen:
        #         return num
        #     else:
        #         seen.add(num)