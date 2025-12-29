class Solution {
 public:
  bool pyramidTransition(string bottom, vector<string>& allowed) {
    for (const string& a : allowed)
      mp[a.substr(0, 2)].push_back(a[2]);

    return dfs(bottom);
  }

 private:
  unordered_map<string, vector<char>> mp;
  unordered_map<string, bool> memo;

  bool dfs(const string& row) {
    if (row.length() == 1)
      return true;

    if (memo.count(row))
      return memo[row];

    return memo[row] = buildNextRow(row, 0, "");
  }

  bool buildNextRow(const string& row, int i, string nextRow) {
    if (i == row.length() - 1)
      return dfs(nextRow);

    string prefix = row.substr(i, 2);
    if (!mp.count(prefix))
      return false;

    for (char c : mp[prefix]) {
      if (buildNextRow(row, i + 1, nextRow + c))
        return true;
    }

    return false;
  }
};
