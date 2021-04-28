class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        while a ** 2 <= c:
            b = sqrt(c - a ** 2)
            if b % 1 == 0:
                return True
            a += 1
        return False