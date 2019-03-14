from typing import List

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        stat0, stat1 = [0] * 26, [0] * 26
        for i, word in enumerate(A):
            if i == 0:
                for ch in word:
                    stat0[ord(ch) - 97] += 1
            else:
                for j in range(26):
                    stat1[j] = 0
                for ch in word:
                    stat1[ord(ch) - 97] += 1
                for j in range(26):
                    stat0[j] = min(stat0[j], stat1[j])
        
        ans = list()
        for i in range(26):
            ans.extend([chr(i + 97)] * stat0[i])
        
        return ans


solution = Solution()
print(solution.commonChars(["bella","label","roller"]))
print(solution.commonChars(["cool","lock","cook"]))
