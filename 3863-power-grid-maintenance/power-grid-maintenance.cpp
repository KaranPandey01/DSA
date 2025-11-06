#include <bits/stdc++.h>
using namespace std;

class DSU {
public:
    vector<int> parent, size;
    DSU(int n) {
        parent.resize(n + 1);
        size.assign(n + 1, 1);
        iota(parent.begin(), parent.end(), 0);
    }

    int find(int x) {
        if (parent[x] == x) return x;
        return parent[x] = find(parent[x]);
    }

    void unite(int a, int b) {
        a = find(a);
        b = find(b);
        if (a == b) return;
        if (size[a] < size[b]) swap(a, b);
        parent[b] = a;
        size[a] += size[b];
    }
};

class Solution {
public:
    vector<int> processQueries(int c, vector<vector<int>>& connections, vector<vector<int>>& queries) {
        DSU dsu(c);

        // Build DSU from connections
        for (auto& edge : connections) {
            dsu.unite(edge[0], edge[1]);
        }

        // Maintain sets of online stations per component
        unordered_map<int, set<int>> onlineSets;
        for (int i = 1; i <= c; ++i) {
            int root = dsu.find(i);
            onlineSets[root].insert(i);
        }

        vector<bool> online(c + 1, true);
        vector<int> results;

        for (auto& q : queries) {
            int type = q[0], x = q[1];
            int root = dsu.find(x);

            if (type == 1) {  // maintenance check
                if (online[x]) {
                    results.push_back(x);
                } else if (!onlineSets[root].empty()) {
                    results.push_back(*onlineSets[root].begin());
                } else {
                    results.push_back(-1);
                }
            } 
            else if (type == 2) {  // go offline
                if (online[x]) {
                    online[x] = false;
                    onlineSets[root].erase(x);
                }
            }
        }

        return results;
    }
};
