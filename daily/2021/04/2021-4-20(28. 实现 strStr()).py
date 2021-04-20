class Solution:
    def getNxt(self, needle: str):
        m = len(needle)
        nxt = [-1] * (m + 1)
        i, j = 0, -1
        while i < m:
            if j == -1 or needle[i] == needle[j]:
                i += 1
                j += 1
                nxt[i] = j
            else:
                j = nxt[j]
        return nxt

    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        if m == 0:
            return 0
        nxt = self.getNxt(needle)
        cnt, i, j = 0, 0, 0
        while i < n:
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = nxt[j]
            if j == m:
                return i - m
        return -1