class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        if len(s)==1:
            return 1

        presence = {}
        start=0
        max_s=0

        for end in range(len(s)):
            if presence.get(s[end]) is None:
                presence[s[end]]=1
            else:
                presence[s[end]]+=1
            print(presence)
            

            while presence.get(s[end])>1:
                presence[s[start]]-=1
                start+=1
            print(presence)
            print(start)
            max_s = max(max_s,end-start+1)

            
        
        return max_s

