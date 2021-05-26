class Solution:
    def reverseParentheses(self, s: str) -> str:
        stk = [[]]
        for c in s:
            if c == '(':
                stk.append([])
            elif c == ')':
                tmp = reversed(stk.pop())
                stk[-1] += tmp
            else:
                stk[-1].append(c)
        return ''.join(stk[0])