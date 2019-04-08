from typing import List

class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        clips_cur = sorted(clips, key=lambda x: x[0])
        l, r, pos = 0, 0, 0
        ans = 0

        while l < T and pos < len(clips):
            pos0 = pos
            while pos < len(clips) and clips_cur[pos][0] <= l:
                r = max(r, clips_cur[pos][1])
                pos += 1
            if pos0 == pos:
                break
            ans += 1
            l = r
            
        return -1 if l < T else ans


solution = Solution()
print(solution.videoStitching([[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]],10))
print(solution.videoStitching([[0,1],[1,2]],5))
print(solution.videoStitching([[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]],9))
print(solution.videoStitching([[0,4],[2,8]],5))
