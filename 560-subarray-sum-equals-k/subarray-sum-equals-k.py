class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        count = 0
        current_sum = 0
        
        # Dictionary to store the frequency of each prefix sum.
        # Initialized with 0: 1 to handle cases where current_sum directly equals k.
        prefix_sums = {0: 1}
        
        # We iterate using a basic loop without len() or range()
        for num in nums:
            current_sum += num
            
            # The value we need to find in our previously seen sums
            diff = current_sum - k
            
            # Check if diff exists using basic 'in' operator (no .get() or .keys() methods)
            if diff in prefix_sums:
                count += prefix_sums[diff]
                
            # Add the current_sum to our dictionary or increment its count
            if current_sum in prefix_sums:
                prefix_sums[current_sum] += 1
            else:
                prefix_sums[current_sum] = 1
                
        return count