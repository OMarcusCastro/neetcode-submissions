class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        

        def dfs(i, isConnected,visits):
            visits[i] = 1
           
            for j in range(len(isConnected[i])):
                if isConnected[i][j]==1 and not visits.get(j):
                    print(j)
                    dfs(j,isConnected,visits)
            
            
        visits = {}
        count=0
        for i in range(len(isConnected)):
            if not visits.get(i):
                count+=1
                dfs(i,isConnected,visits)
        return count
            