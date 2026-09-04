class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_seen = {}

        for i in range(len(nums)):
            val = nums[i]

            if val in last_seen and (i - last_seen[val]) <= k:
                return True
            last_seen[val] = i
        
        return False