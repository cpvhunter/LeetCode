#include <vector>
#include <queue>
#include <unordered_set>

using namespace std;

#define LL long long
#define PII pair<int, int>

class Solution {
private:
    const static int X_MIN = 0;
    const static int X_MAX = 1000000 - 1;
    const static int Y_MIN = 0;
    const static int Y_MAX = 1000000 - 1;
    const static vector<vector<int>> DIRECTIONS;
    
public:
    LL encrypt(int x, int y) {
        return (((LL)x) << 20) + y;
    }
    
    bool success(const unordered_set<LL>& s_blocked, const vector<int>& source, const vector<int>& target, int max_step) {
        queue<PII> q;
        q.push(make_pair(source[0], source[1]));
        unordered_set<LL> used;
        used.insert(encrypt(source[0], source[1]));
        
        int cur_step = 1;
        while (!q.empty() && cur_step <= max_step) {
            PII node = q.front();
            q.pop();
            int x = node.first;
            int y = node.second;
            for (const vector<int>& dir: DIRECTIONS) {
                int nx = x + dir[0];
                int ny = y + dir[1];
                if (nx >= X_MIN && nx <= X_MAX && ny >= Y_MIN && ny <= Y_MAX) {
                    LL enc = encrypt(nx, ny);
                    if (!s_blocked.count(enc) && !used.count(enc)) {
                        ++cur_step;
                        q.push(make_pair(nx, ny));
                        used.insert(enc);
                        if (nx == target[0] && ny == target[1]) {
                            return true;
                        }
                    }
                }
            }
        }
        return cur_step > max_step;
    }
    
    bool isEscapePossible(vector<vector<int>>& blocked, vector<int>& source, vector<int>& target) {
        unordered_set<LL> s_blocked;
        for (const vector<int>& v: blocked) {
            s_blocked.insert(encrypt(v[0], v[1]));
        }
        int max_step = (blocked.size() - 1) * blocked.size() / 2 + 1;
        return success(s_blocked, source, target, max_step) && success(s_blocked, target, source, max_step);
    }
};

const vector<vector<int>> Solution::DIRECTIONS = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
