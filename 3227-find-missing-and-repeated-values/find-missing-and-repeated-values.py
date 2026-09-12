class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        total_ele = len(grid) ** 2

        ans = []
        idx = [0] * 2


        for i in range(len(grid)):
            for j in range(len(grid[i])):
                ans.append(grid[i][j])
                
        ans.sort()
        i = 0

        while i < (total_ele - 1):
            j = i + 1
            while j < total_ele:
                if ans[i] == ans[j]:
                    idx[0] = ans[j]
                j += 1
            i += 1

        for i in range(1, total_ele + 1):
            if i not in ans:
                idx[1] = i

        return idx