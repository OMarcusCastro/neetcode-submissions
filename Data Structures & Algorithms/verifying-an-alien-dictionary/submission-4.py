class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        i = 0;
        mapper = {}
        for letter in order:
            mapper[letter] = i
            i+=1
        
        if len(words)<2:
            return True
        
        for i in range(len(words)-1):
            curr_word = words[i]
            next_word = words[i+1]
            for j in range(len(curr_word)):
                
                if mapper[curr_word[j]]<mapper[next_word[j]]:
                    break
                
                if j+1>len(next_word)-1:
                    return False
                if mapper[curr_word[j]]>mapper[next_word[j]]:
                    return False
                
        
        return True






