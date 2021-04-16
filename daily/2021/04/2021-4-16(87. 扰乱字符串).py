class Solution:
    @cache
    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2):
            return False
        for l in range(1, n):
            if self.isScramble(s1[:l], s2[:l]) and self.isScramble(s1[l:], s2[l:]):
                return True
            if self.isScramble(s1[:l], s2[-l:]) and self.isScramble(s1[l:], s2[:-l]):
                return True
        return False