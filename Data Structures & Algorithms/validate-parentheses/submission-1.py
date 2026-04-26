class Solution:
    def isValid(self, s: str) -> bool:  
        #size s ==1 invalid
        #close match with last in the stack
        char_map = {
            "(":")",
            "{":"}",
            "[":"]",
        }
        stack = []

        for c in s:
            #if open char -> add to stack
            #if close char -> remove of stack the same
                #if diferrent return false
            
            if char_map.get(c) is not None:
                stack.append(c)
            else:
                if len(stack)==0 or char_map.get(stack[-1])!=c :
                    return False
                stack.pop()
        
        return len(stack)==0