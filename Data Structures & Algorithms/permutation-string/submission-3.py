class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map ={}
        s2_map = {}
        for latter in s1:
            s1_map[latter] = 1+s1_map.get(latter,0)
  
        start = 0
        max_size =0
        ans = False
        for end in range(len(s2)):
            curr = s2[end]
            s2_map[curr] = 1+s2_map.get(curr,0)
        
            

            while s2_map.get(curr)>s1_map.get(curr,0):
                s2_map[s2[start]]-=1
                start+=1
                

            if s2_map[curr]==0:
                    del s2_map[curr]
            max_size = max(max_size,end-start+1)

        

        return max_size==len(s1)
        