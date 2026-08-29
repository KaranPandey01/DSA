class Solution:
    def lexicographicallySmallestArray(self, nums: list[int], limit: int) -> list[int]:
        sorted_pairs = sorted((val, idx) for idx, val in enumerate(nums))
        groups = []
        
        for val, idx in sorted_pairs:
            if not groups or val - groups[-1][-1][0] > limit:
                groups.append([])
            groups[-1].append((val, idx))
            
        result = [0] * len(nums)
        
        for group in groups:
            vals = [val for val, idx in group]
            indices = sorted([idx for val, idx in group])
            
            for val, idx in zip(vals, indices):
                result[idx] = val
                
        return result
