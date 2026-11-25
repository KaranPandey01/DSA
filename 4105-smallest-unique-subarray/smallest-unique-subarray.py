from collections import Counter


class Solution:
    def smallestUniqueSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        mod1, mod2 = 1_000_000_007, 1_000_000_009
        base1, base2 = 100_003, 100_019

        p1 = [1] * (n + 1)
        p2 = [1] * (n + 1)
        h1 = [0] * (n + 1)
        h2 = [0] * (n + 1)

        for i, val in enumerate(nums):
            p1[i + 1] = (p1[i] * base1) % mod1
            p2[i + 1] = (p2[i] * base2) % mod2
            h1[i + 1] = (h1[i] * base1 + val) % mod1
            h2[i + 1] = (h2[i] * base2 + val) % mod2

        def has_unique_of_len(length: int) -> bool:
            counts = Counter()
            for i in range(n - length + 1):
                j = i + length
                sub1 = (h1[j] - h1[i] * p1[length]) % mod1
                sub2 = (h2[j] - h2[i] * p2[length]) % mod2
                counts[(sub1, sub2)] += 1
            return any(cnt == 1 for cnt in counts.values())

        low, high = 1, n
        ans = n
        while low <= high:
            mid = (low + high) // 2
            if has_unique_of_len(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
