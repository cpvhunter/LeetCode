class Solution:
    def clumsy(self, N: int) -> int:
        op = ["*", "//", "+", "-"]
        expr = ""
        for i in range(N, 0, -1):
            expr += str(i)
            if i > 1:
                expr += op[(N - i) % 4]
        return eval(expr)


solution = Solution()
print(solution.clumsy(4))
print(solution.clumsy(10))
