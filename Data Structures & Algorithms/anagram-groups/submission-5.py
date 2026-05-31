class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_array = []
        for word in strs:
            freq = {}
            for char in word:
                freq[char] = freq.get(char, 0) + 1
            freq_array.append(freq)

        ans = {}
        for i, word in enumerate(strs):
            key = tuple(sorted(freq_array[i].items()))
            ans[key] = ans.get(key, []) + [word]

        return list(ans.values())