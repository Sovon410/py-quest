# from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # Slow - Fast pointer.........

        # Phase 1: Finding the intersection point in the cycle
        slow = nums[0]
        fast = nums[0]
        
        while True:
            slow = nums[slow]          # 1 step
            fast = nums[nums[fast]]    # 2 steps
            if slow == fast:
                break
                
        # Phase 2: Finding the entrance to the cycle (the duplicate)
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]          # 1 step
            fast = nums[fast]          # 1 step
            
        return slow

# ===================================== OR ===========================================

        # seen = [0] * (len(nums) + 1)

        # for num in nums:
        #     seen[num] += 1

        # for num in range(1, len(nums) + 1):
        #     if seen[num] > 1:
        #         return num

# ===================================== OR =======================================

        # seen = set()

        # for num in nums:
        #     if num in seen:
        #         return num
        #     else:
        #         seen.add(num)