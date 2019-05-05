from typing import List

class Solution:
    DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def __init__(self):
        self.used = set()
    
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        
        def is_border(x, y):
            return x == 0 or x == m - 1 or y == 0 or y == n - 1 or grid[x - 1][y] != grid[x][y] or grid[x + 1][y] != grid[x][y] or grid[x][y - 1] != grid[x][y] or grid[x][y + 1] != grid[x][y]
        
        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or (x, y) in self.used or grid[x][y] != grid[r0][c0]:
                return
            self.used.add((x, y))
            for dx, dy in Solution.DIRS:
                dfs(x + dx, y + dy)
        
        dfs(r0, c0)
        ret = [[x for x in row] for row in grid]
        for x, y in self.used:
            if is_border(x, y):
                ret[x][y] = color
        
        return ret


solution = Solution()
print(solution.colorBorder([[1,1],[1,2]],0,0,3))
print(solution.colorBorder([[1,2,2],[2,3,2]],0,1,3))
print(solution.colorBorder([[1,1,1],[1,1,1],[1,1,1]],1,1,2))
