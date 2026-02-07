class Solution {
public:
    int minimumDeletions(string s) {
        int stringLength = s.size();
      
        // dp[i] represents the minimum deletions needed to make s[0...i-1] balanced
        // where balanced means no 'b' appears before any 'a'
        vector<int> dp(stringLength + 1, 0);
      
        // Count of 'b' characters seen so far
        int bCount = 0;
      
        // Iterate through each character in the string
        for (int i = 1; i <= stringLength; ++i) {
            if (s[i - 1] == 'b') {
                // If current character is 'b', it doesn't violate the balance
                // So minimum deletions remain the same as previous state
                dp[i] = dp[i - 1];
                bCount++;
            } else {
                // If current character is 'a', we have two choices:
                // 1. Delete this 'a' (cost: dp[i-1] + 1)
                // 2. Keep this 'a' and delete all 'b's before it (cost: bCount)
                // Choose the minimum cost option
                dp[i] = min(dp[i - 1] + 1, bCount);
            }
        }
      
        return dp[stringLength];
    }
};