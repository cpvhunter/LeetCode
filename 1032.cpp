#include <string>
#include <vector>

using namespace std;

#define PII pair<int, int>

struct TrieNode {
    int nxt[26];
    int fa;
    int fail;
    bool isend;
    TrieNode(int _fa): isend(false), fa(_fa), fail(0) {
        memset(nxt, -1, sizeof(nxt));
    }
};

class StreamChecker {
public:
    vector<TrieNode> trie;
    int root;
    int querypos;
    
public:
    StreamChecker(vector<string>& words) {
        root = querypos = 0;
        trie.push_back(TrieNode(-1));
        
        for (const string& word: words) {
            int cur = root;
            for (const char& ch: word) {
                if (trie[cur].nxt[ch - 97] == -1) {
                    trie.push_back(TrieNode(cur));
                    trie[cur].nxt[ch - 97] = (int)trie.size() - 1;
                }
                cur = trie[cur].nxt[ch - 97];
            }
            trie[cur].isend = true;
        }
        
        buildfail();
    }
    
    void buildfail() {
        queue<PII> q;
        for (int i = 0; i < 26; ++i) {
            if (trie[root].nxt[i] != -1) {
                q.push(make_pair(trie[root].nxt[i], i));
            }
        }
        
        while (!q.empty()) {
            int node = q.front().first;
            int idx = q.front().second;
            q.pop();
            
            int cur = trie[trie[node].fa].fail;
            while (cur) {
                if (trie[cur].nxt[idx] == -1) {
                    cur = trie[cur].fail;
                }
                else {
                    break;
                }
            }
            if (trie[cur].nxt[idx] != -1 && trie[cur].nxt[idx] != node) {
                trie[node].fail = trie[cur].nxt[idx];
                trie[node].isend |= trie[trie[cur].nxt[idx]].isend;
            }
            else {
                trie[node].fail = root;
            }
            
            for (int i = 0; i < 26; ++i) {
                if (trie[node].nxt[i] != -1) {
                    q.push(make_pair(trie[node].nxt[i], i));
                }
            }
        }
    }
    
    bool query(char letter) {
        while (querypos != root && trie[querypos].nxt[letter - 97] == -1) {
            querypos = trie[querypos].fail;
        }
        if (trie[querypos].nxt[letter - 97] != -1) {
            querypos = trie[querypos].nxt[letter - 97];
        }
        return trie[querypos].isend;
    }
};