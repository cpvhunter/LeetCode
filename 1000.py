from typing import List

class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        n = len(stones)
        if K > 2 and n % (K - 1) != 1:
            return -1
        
        f = [[0] * n for _ in range(n)]
        ssum = [0] * (n + 1)
        for i in range(n):
            f[i][i] = 0 # stones[i]
            ssum[i + 1] = ssum[i] + stones[i]
        
        for l in range(2, n + 1):
            p = (l - 1) % (K - 1) + 1
            for i in range(n - l + 1):
                j, k = i + l - 1, i + l - 2
                f[i][j] = 99999999
                while k - i + 1 >= p - 1:
                    cost = f[i][k] + f[k + 1][j]
                    if p == 1:
                        cost += ssum[j + 1] - ssum[i]
                    f[i][j] = min(f[i][j], cost)
                    k -= (K - 1)
                
        return f[0][n - 1]


solution = Solution()
print(solution.mergeStones([3,2,4,1],2))
print(solution.mergeStones([3,2,4,1],3))
print(solution.mergeStones([3,5,1,2,6],3))
