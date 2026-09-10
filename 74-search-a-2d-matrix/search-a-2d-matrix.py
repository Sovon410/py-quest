class Solution:

    def search_in_row(self, matrix: List[List[int]], target: int, row: int) -> bool:
        n = len(matrix[0])
        st = 0
        end = n - 1

        while st <= end:
            mid = st + (end - st) // 2
            if target == matrix[row][mid]:
                return True
            elif target > matrix[row][mid]:
                st = mid + 1
            else:
                end = mid - 1
            
        return False


    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        start_row, end_row = 0, m - 1

        while start_row <= end_row:
            mid_row = start_row + (end_row - start_row) // 2

            if target >= matrix[mid_row][0] and target <= matrix[mid_row][n - 1]:
                return self.search_in_row(matrix, target, mid_row)

            elif target > matrix[mid_row][n - 1]:
                start_row = mid_row + 1
            else:
                end_row = mid_row - 1
    
        return False
