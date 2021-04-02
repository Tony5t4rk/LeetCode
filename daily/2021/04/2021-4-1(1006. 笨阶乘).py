class Solution:
    def clumsy(self, N: int) -> int:
        stack = []
        sign = '*'
        cur = N
        for num in range(N - 1, 0, -1):
            if sign == '*':
                cur = cur * num
                sign = '/'
            elif sign == '/':
                cur = cur // num
                sign = '+'
            elif sign == '+':
                stack.append(cur)
                stack.append(num)
                cur = 0
                sign = '-'
            elif sign == '-':
                cur = num
                sign = '*'
        stack.append(cur)
        result = stack[0]
        for i in range(1, len(stack), 2):
            result += stack[i]
            if i + 1 < len(stack):
                result -= stack[i + 1]
        return result