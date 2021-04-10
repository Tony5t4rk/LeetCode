class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0:
            return False
        xs = [2, 3, 5]
        for x in xs:
            while n % x == 0:
                n //= x
        return n == 1