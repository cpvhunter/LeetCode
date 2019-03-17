import math

class Solution:
    def bitwiseComplement(self, N: int) -> int:
        return 1 if N == 0 else 2**int(math.log2(N) + 1) - 1 - N


solution = Solution()
print(solution.bitwiseComplement(5))
print(solution.bitwiseComplement(7))
print(solution.bitwiseComplement(10))
