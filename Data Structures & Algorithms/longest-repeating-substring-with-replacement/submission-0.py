class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequence = {}
        start = 0
        max_ =0
        more_freq=0
        for end in range(len(s)):
            latter = s[end]
            frequence[latter] = 1+frequence.get(latter,0)
            
            more_freq = max(frequence[latter],more_freq)

            while end-start+1-more_freq>k:
                frequence[s[start]]-=1
                start+=1

            max_ = max(max_,end-start+1)
    
        return max_




