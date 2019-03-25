class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        ans, cur = 0, 0
        set_mod = set()

        while True:
            cur = (cur * 10 + 1) % K
            ans += 1
            if cur in set_mod:
                return -1
            if cur == 0:
                return ans
            set_mod.add(cur)


solution = Solution()
print(solution.smallestRepunitDivByK(1))
print(solution.smallestRepunitDivByK(2))
print(solution.smallestRepunitDivByK(3))