class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        result = []
        s_row, s_col, e_row, e_col = 0, 0, m - 1, n - 1

        while s_row <= e_row and s_col <= e_col:
            # Top...
            for i in range(s_col, e_col + 1):
                result.append(matrix[s_row][i])

            # Right...
            for i in range(s_row + 1, e_row + 1):
                result.append(matrix[i][e_col])

            # Bottom...
            for i in range(e_col - 1, s_col - 1, -1):
                if s_row == e_row:
                    break
                result.append(matrix[e_row][i])

            # Left...
            for i in range(e_row - 1, s_row, -1):
                if s_col == e_col:
                    break
                result.append(matrix[i][s_col])

            s_row += 1
            s_col += 1
            e_row -= 1
            e_col -= 1

        return result