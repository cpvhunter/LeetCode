from typing import List

class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        n = len(stones)
        stones.sort()
        max_move = max(stones[-1] - stones[1] + 2 - n, stones[-2] - stones[0] + 2 - n)
        min_move = max_move
        l = 0
        for r in range(n):
            while stones[r] - stones[l] + 1 > n:
                l += 1
            if stones[r] - stones[l] + 1 == n - 1 and r - l + 1 == n - 1:
                min_move = min(min_move, 2)
            else:
                min_move = min(min_move, n - (r - l + 1))
        
        return [min_move, max_move]


solution = Solution()
print(solution.numMovesStonesII([1,2,3,7,8,9]))
print(solution.numMovesStonesII([7,4,9]))
print(solution.numMovesStonesII([6,5,4,3,10]))
print(solution.numMovesStonesII([100,101,104,102,103]))
