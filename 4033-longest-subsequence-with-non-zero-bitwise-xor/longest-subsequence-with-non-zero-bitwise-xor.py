class Solution:
    def longestSubsequence(self, nums: list[int]) -> int:
        total_xor = 0
        has_nonzero = False
        
        for num in nums:
            total_xor ^= num
            if num > 0:
                has_nonzero = True
        
        # Case 1: All elements are 0
        if not has_nonzero:
            return 0
        
        # Case 2: Entire array XOR sum is already non-zero
        if total_xor != 0:
            return len(nums)
        
        # Case 3: Entire array XOR sum is 0, remove 1 non-zero element
        return len(nums) - 1
