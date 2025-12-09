#include <vector>
#include <numeric>

using namespace std;

class Solution {
public:
    int specialTriplets(vector<int>& nums) {
        long long MOD = 1e9 + 7;
        int n = nums.size();
        
        // Max value of nums[i] is 10^5. Max target value `2 * nums[j]` is 2*10^5.
        // Frequency array must be large enough to hold counts for these values.
        int freq_array_size = 2 * 100000 + 1;
        
        vector<long long> left_counts(freq_array_size, 0);
        vector<long long> right_counts(freq_array_size, 0);
        
        // Initially, all numbers are in the "right" partition.
        for (int num : nums) {
            right_counts[num] += 1;
        }
        
        long long total_triplets = 0;
        
        // Iterate through each element, considering it as the middle element nums[j].
        for (int val_j : nums) {
            // Move the current element from the right partition to the left.
            // First, remove it from right_counts for the current calculation.
            right_counts[val_j] -= 1;
            
            int target_val = 2 * val_j;
            
            // Since max(nums[i])=10^5, target_val <= 200000, which is a valid index.
            long long count_i = left_counts[target_val];
            long long count_k = right_counts[target_val];
                
            long long term = count_i * count_k;
            total_triplets = (total_triplets + term) % MOD;
            
            // Now, add the current element to left_counts for subsequent iterations.
            left_counts[val_j] += 1;
        }
        
        return (int)total_triplets;
    }
};