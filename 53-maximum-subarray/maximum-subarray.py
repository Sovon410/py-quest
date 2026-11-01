class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        lnt = len(nums)
        start = 0
        end = 0
        temp_start = 0
        
        current_sum = nums[0]
        max_sum = nums[0]

        if lnt == 1:
            return max_sum
        else:
            for i in range(1, lnt):
                if nums[i] > current_sum + nums[i]:
                    current_sum = nums[i]
                    temp_start = i
                else:
                    current_sum += nums[i]
                
                if current_sum > max_sum:
                    max_sum = current_sum
                    start = temp_start
                    end = i
        return max_sum