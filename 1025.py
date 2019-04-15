class Solution:
    def divisorGame(self, N: int) -> bool:
        f = [False] * (N + 1)
        for i in range(2, N + 1):
            for j in range(1, i):
                if i % j == 0 and f[i - j] == False:
                    f[i] = True
                    break
        return f[N]


solution = Solution()
print(solution.divisorGame(2))
print(solution.divisorGame(3))
