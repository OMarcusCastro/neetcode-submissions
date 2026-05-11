class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        l,r = 0,0
        l_max = 0
        r_max = 0
        size = 0
        for i in range(len(s)):
            l,r = i,i
            while s[l]==s[r]:
                if r-l>=r_max-l_max:
                    r_max,l_max=r,l
                # print(l_max,r_max)

                l-=1
                r+=1
                if l<0 or r>len(s)-1:
                    break

        print(s[l_max:r_max+1])
        for i in range(len(s)-1):
            l,r = i,i+1
            while s[l]==s[r]:
                if r-l>=r_max-l_max:
                    r_max,l_max=r,l
                # print(l_max,r_max)

                l-=1
                r+=1
                if l<0 or r>len(s)-1:
                    break
        # print(l_max,r_max)
        return s[l_max:r_max+1]
                

