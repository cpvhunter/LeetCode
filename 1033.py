from typing import List

class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        x = min(min(a, b), c)
        z = max(max(a, b), c)
        y = a + b + c - x - z
        if y - x == 1 and z - y == 1:
            return [0, 0]
        elif y - x > 2 and z - y > 2:
            return [2, z - x - 2]
        else:
            return [1, z - x - 2]


solution = Solution()
print(solution.numMovesStones(1,2,5))
print(solution.numMovesStones(4,3,2))
print(solution.numMovesStones(3,5,1))
