class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        i = 0
        currLine, currSize = [],0
       
           
        while i < len(words):

            if currSize+len(currLine)+len(words[i])<=maxWidth:

                currLine.append(words[i])
                currSize+= len(words[i])
                i+=1
            else:

                spaces = (maxWidth-currSize)//max(1,len(currLine)-1)
                remainder = (maxWidth-currSize)%max(1,len(currLine)-1)

                

                for j in range(max(1,len(currLine)-1)):
                    currLine[j]+=" "*spaces
                    if remainder>0:
                        currLine[j]+=" "
                        remainder-=1
                ans.append("".join(currLine))    
                currLine =[]
                currSize = 0

        lastLine = " ".join(currLine)
        spaces = maxWidth - len(lastLine)
        ans.append(lastLine+" "*spaces)
        
            


        return ans