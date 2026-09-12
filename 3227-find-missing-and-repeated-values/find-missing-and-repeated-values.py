class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        total_ele = len(grid) ** 2 + 1
        freq = [0] * total_ele

        for row in grid:
            for val in row:
                freq[val] += 1
        
        repeated = -1
        missing = -1

        for i in range(1, total_ele):
            if freq[i] == 2:
                repeated = i
            elif freq[i] == 0:
                missing = i

        return [repeated, missing]