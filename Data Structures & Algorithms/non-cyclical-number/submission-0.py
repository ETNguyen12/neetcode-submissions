class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def sum_squares(n: int) -> int:
            res = 0
            while n > 0:
                digit = n % 10
                res += digit * digit
                n = n // 10
            return res

        while n not in seen:
            seen.add(n)
            n = sum_squares(n)
            if n == 1:
                return True
        return False
            