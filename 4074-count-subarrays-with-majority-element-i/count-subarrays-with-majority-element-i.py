class Solution:
    def countMajoritySubarrays(self, nums, target):
        n = len(nums)
        result = 0

        def is_majority(freq, total):
            got = freq.get(target, 0)
            needed = total // 2 + 1
            return got >= needed

        i = 0
        while i < n:
            freq = {}
            j = i
            sz = 0

            while j < n:
                k = nums[j]
                if k in freq:
                    freq[k] += 1
                else:
                    freq[k] = 1
                sz += 1

                if is_majority(freq, sz):
                    result += 1

                j += 1

            freq.clear()
            i += 1

        return result