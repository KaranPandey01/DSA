class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        counts={}

        for ch in s:
            if ch in counts:
                counts[ch]+=1
            else:
                counts[ch] = 1
        
        for ch in t:
            if ch in counts:
                counts[ch] -= 1

                if counts[ch]<0:
                    return False
            else:
                return False

        return True