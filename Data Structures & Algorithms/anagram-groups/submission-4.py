class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqArray =[]
        for i in range(len(strs)):
            word = strs[i]
            freq={}
            for latter in word:
                freq[latter] = freq.get(latter,0)+1
            freqArray.append(freq)

        ans = []
        for i in range(len(strs)):
            if strs[i]=="0":
                continue
            array = [strs[i]]
            for j in range(i+1,len(strs)):
                if freqArray[i]==freqArray[j]:
                    array.append(strs[j])
                    strs[j] ="0"
            ans.append(array)
        return ans