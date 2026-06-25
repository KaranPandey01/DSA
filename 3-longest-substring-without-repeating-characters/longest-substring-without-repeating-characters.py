class Solution:
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0

        best = 0
        left = 0
        seen = {}

        right = 0
        while right < len(s):
            ch = s[right]

            if ch in seen and seen[ch] >= left:
                left = seen[ch] + 1

            seen[ch] = right
            curr = right - left + 1

            if curr > best:
                best = curr

            right += 1

        return best