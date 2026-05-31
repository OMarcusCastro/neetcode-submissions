def createAdj(prerequisites):
    adj = {}
    for a,b in (prerequisites):
        adj[a] = adj.get(a,[])+[b]
    return adj

def dfs(curr,adj,visits,visiting,topSort):
    if visiting.get(curr,0)==1:
        return False

    visiting[curr] = 1
    if visits.get(curr,0)==1:
        return True
    visits[curr] = 1
    
    # if adj.get(curr) is None:
    #     topSort.append(curr)
        
    #     return True

    for nei in adj.get(curr,[]):
        if dfs(nei,adj,visits,visiting,topSort) is False:
            return False
    
    topSort.append(curr)
    visiting[curr]=0



class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visits = {}
        topSort =[]
        adj = createAdj(prerequisites)
        for i in range(numCourses):
            if visits.get(i,0)==0:
                if dfs(i,adj,visits,{},topSort) is False:
                    return []
        # print(topSort)
        return topSort