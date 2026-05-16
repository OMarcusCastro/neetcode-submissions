class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            freq[s[i]] = freq.get(s[i],0)+1
        
        for i in range(len(s)):

            if not freq.get(t[i]):
                return False
            if freq[t[i]] <0:
                return False
            freq[t[i]]-=1
        return True
            
