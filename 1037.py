from typing import List

class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        a = points
        return (a[1][1] - a[0][1]) * (a[2][0] - a[1][0]) != (a[2][1] - a[1][1]) * (a[1][0] - a[0][0])


solution = Solution()
print(solution.isBoomerang([[1,1],[2,3],[3,2]]))
print(solution.isBoomerang([[1,1],[2,2],[3,3]]))
