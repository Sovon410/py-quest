class Solution:
    def maxSum(self, nums: List[int]) -> int:
        max_digit_map = {}
        max_sum = -1

        for num in nums:
            max_digit = max(int(d) for d in str(num))
            
            if max_digit in max_digit_map:
                current_sum = num + max_digit_map[max_digit]
                max_sum = max(max_sum, current_sum)
                
            max_digit_map[max_digit] = max(
                max_digit_map.get(max_digit, 0), num
            )
        return max_sum