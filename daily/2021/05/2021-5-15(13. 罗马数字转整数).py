class Solution:
    def romanToInt(self, s: str) -> int:
        mp = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        n = len(s)
        i, ans = 0, 0
        while i < n:
            if i + 1 < n and mp[s[i]] < mp[s[i + 1]]:
                ans += mp[s[i + 1]] - mp[s[i]]
                i += 2
            else:
                ans += mp[s[i]]
                i += 1
        return ans