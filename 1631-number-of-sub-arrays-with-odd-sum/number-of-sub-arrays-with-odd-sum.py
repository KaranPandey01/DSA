class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        even_count = 1  # Accounts for initial prefix sum of 0
        odd_count = 0
        prefix_sum = 0
        result = 0

        for num in arr:
            prefix_sum += num
            if prefix_sum % 2 == 1:
                result = (result + even_count) % MOD
                odd_count += 1
            else:
                result = (result + odd_count) % MOD
                even_count += 1

        return result
