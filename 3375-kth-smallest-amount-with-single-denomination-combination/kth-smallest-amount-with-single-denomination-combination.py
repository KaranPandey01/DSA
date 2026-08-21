import math
from typing import List

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        
        # Helper function to count valid amounts <= x using PIE
        def count_amounts_le(x: int) -> int:
            total_count = 0
            # 1 << n gives total 2^n subsets. Start from 1 to skip the empty subset.
            for mask in range(1, 1 << n):
                current_lcm = 1
                subset_size = 0
                
                for i in range(n):
                    if (mask >> i) & 1:
                        subset_size += 1
                        # Calculate LCM of current subset
                        current_lcm = (current_lcm * coins[i]) // math.gcd(current_lcm, coins[i])
                
                # Inclusion-Exclusion logic
                multiples = x // current_lcm
                if subset_size % 2 == 1:
                    total_count += multiples
                else:
                    total_count -= multiples
            return total_count

        # Binary Search boundaries
        low = 1
        high = k * min(coins)
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            if count_amounts_le(mid) >= k:
                ans = mid
                high = mid - 1  # Try to find a smaller valid amount
            else:
                low = mid + 1   # Increase the range
                
        return ans
