class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        lnt = len(nums)
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        for key in freq.keys():
            if freq[key] > lnt / 2:
                return key
