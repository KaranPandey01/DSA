class Solution {
public:
    int stoneGameV(vector<int>& stoneValue) {
        const int n = stoneValue.size();
        vector<vector<int>> mem(n, vector<int>(n, -1));
        vector<int> prefix(n + 1, 0);
        for (int k = 0; k < n; ++k) {
            prefix[k + 1] = prefix[k] + stoneValue[k];
        }
        return dfs(stoneValue, 0, n - 1, prefix, mem);
    }

private:
    int dfs(const vector<int>& a, int i, int j, const vector<int>& prefix, vector<vector<int>>& mem) {
        if (i == j) return 0;
        if (mem[i][j] != -1) return mem[i][j];
        
        int ans = 0;
        for (int k = i; k < j; ++k) {
            int leftSum = prefix[k + 1] - prefix[i];
            int rightSum = prefix[j + 1] - prefix[k + 1];
            
            if (leftSum < rightSum) {
                ans = max(ans, leftSum + dfs(a, i, k, prefix, mem));
            } else if (leftSum > rightSum) {
                ans = max(ans, rightSum + dfs(a, k + 1, j, prefix, mem));
            } else {
                ans = max(ans, leftSum + max(dfs(a, i, k, prefix, mem), dfs(a, k + 1, j, prefix, mem)));
            }
        }
        return mem[i][j] = ans;
    }
};
