class Solution:
    def queryString(self, S: str, N: int) -> bool:
        a = [int(x) for x in S]
        s = set()
        n = len(a)

        for i in range(n):
            cur = 0
            for j in range(i, n):
                cur = cur * 2 + a[j]
                if cur > N:
                    break
                if cur > 0:
                    s.add(cur)

        return len(s) == N


solution = Solution()
print(solution.queryString("0110", 3))
print(solution.queryString("0110", 4))
