class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.ans = []
        def dfs(i,curr,n,k):
            
            if len(curr)==k:
                self.ans.append(curr.copy())
                return
            
            if i >n or len(curr)>k:
                return 

            curr.append(i)
            # print(curr)
            dfs(i+1,curr,n,k)
            curr.pop()
            dfs(i+1,curr,n,k)
            
        dfs(1,[],n,k)
        return self.ans