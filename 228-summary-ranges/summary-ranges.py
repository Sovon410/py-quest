class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        ranges = []
        if not nums:
            return ranges
        
        start = nums[0]
        
        # Loop one extra time to handle the final range easily
        for i in range(1, len(nums) + 1):
            # Trigger if we are at the end OR the streak breaks
            if i == len(nums) or nums[i] != nums[i-1] + 1:
                # Format the string based on whether start equals end
                if start == nums[i-1]:
                    ranges.append(str(start))
                else:
                    ranges.append(f"{start}->{nums[i-1]}")
                
                # Reset start for the next streak
                if i < len(nums):
                    start = nums[i]
                    
        return ranges