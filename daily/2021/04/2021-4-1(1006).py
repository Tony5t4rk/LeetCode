class Solution:
    def clumsy(self, N: int) -> int:
        stack = []
        def next_sign(x):
            if x == '*':
                return '/'
            elif x == '/':
                return '+'
            elif x == '+':
                return '-'
            return '*'
        sign = '*'
        cur = N
        for num in range(N - 1, 0, -1):
            if sign == '*':
                cur = cur * num
            elif sign == '/':
                cur = cur // num
            elif sign == '+':
                stack.append(cur)
                stack.append(num)
                cur = 0
            elif sign == '-':
                cur = num
            sign = next_sign(sign)
        stack.append(cur)
        result = stack[0]
        for i in range(1, len(stack), 2):
            result += stack[i]
            if i + 1 < len(stack):
                result -= stack[i + 1]
        return result