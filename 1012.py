class Solution:
    def numDupDigitsAtMostN(self, N: int) -> int:
        def P(m, n):
            ret = 1
            for i in range(n):
                ret *= m - i
            return ret

        if N < 10:
            return 0

        a = [int(x) for x in str(N)]
        digit = set()
        ans = 0
        for i in range(1, len(a)):
            ans += 9 * P(9, i - 1)
        
        for i in range(len(a)):
            cnt = 0
            for j in range(a[i]):
                if i + j > 0 and j not in digit:
                    cnt += 1
            ans += cnt * P(9 - i, len(a) - i - 1)

            if a[i] in digit:
                break
            digit.add(a[i])
            if i == len(a) - 1:
                ans += 1
        
        return N - ans


solution = Solution()
print(solution.numDupDigitsAtMostN(20))
print(solution.numDupDigitsAtMostN(100))
print(solution.numDupDigitsAtMostN(1000))
