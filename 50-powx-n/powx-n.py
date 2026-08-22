class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if x == 0:
            return 0
        if x == 1:
            return 1
        if (x == -1 and n % 2 == 0):
            return 1
        if (x == -1 and n % 2 != 0):
            return -1

        bin_form = n
        answer = 1

        if n < 0:
            x = 1/x
            bin_form = -bin_form

        while(bin_form > 0):
            if(bin_form % 2 == 1):
                answer *= x
            x *= x
            bin_form //= 2
        return answer