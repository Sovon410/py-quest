class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        rev_num = 0

        INT_MAX = 2 ** 31 - 1

        while x != 0:
            digit = x % 10
            x //= 10

            if rev_num > (INT_MAX - digit) // 10:
                return 0
            rev_num = rev_num * 10 + digit
        
        result = sign * rev_num
        
        return result if -2**31 <= result <= 2**31 - 1 else 0