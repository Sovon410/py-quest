class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1
        if x == 1:
            return 1

        m = abs(n)
        ans = 1

        while m > 0:
            if m % 2 == 1:
                ans *= x
            x *= x
            m //= 2
        
        return 1 / ans if n < 0 else ans