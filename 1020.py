from typing import List

class Solution:
    DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def numEnclaves(self, A: List[List[int]]) -> int:
        def bfs(A, used, x, y, m, n):
            used[x][y] = True
            position = [(x, y)]
            head, tail, escape = 0, 0, False
            
            while head <= tail:
                curx, cury = position[head]
                head += 1
                for direct in self.DIRECTIONS:
                    nextx, nexty = curx + direct[0], cury + direct[1]
                    if nextx < 0 or nextx >= m or nexty < 0 or nexty >= n:
                        escape = True
                    elif A[nextx][nexty] == 1 and used[nextx][nexty] == False:
                        used[nextx][nexty] = True
                        position.append((nextx, nexty))
                        tail += 1
            return 0 if escape else len(position)
        
        m, n = len(A), len(A[0])
        used = [[False] * n for _ in range(m)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    if not used[i][j]:
                        ans += bfs(A, used, i, j, m, n)
        return ans


solution = Solution()
print(solution.numEnclaves([[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]))
print(solution.numEnclaves([[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]))
