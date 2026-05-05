class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW =len(grid)-1
        COL = len(grid[0])-1
        def dfs(r,c,grid,dfs_vist):
            # print(grid)
            r = int(r)
            c = int(c)
            # ROW =len(grid)
            # COL = len(grid[0])-1
            if min(r,c)<0 or r>ROW or c>COL or (r,c) in dfs_vist or grid[r][c]=="0":
                return
            

            dfs_vist.add((r,c))
            dfs(r+1,c,grid,dfs_vist)
            dfs(r-1,c,grid,dfs_vist)
            dfs(r,c+1,grid,dfs_vist)
            dfs(r,c-1,grid,dfs_vist)
            dfs_vist.remove((r,c))
            grid[r][c]="0"
            return
        count =0
        for r in range(ROW+1):
            for c in range(COL+1):
                if grid[r][c]=="1":
                    count+=1
                    dfs(r,c,grid,set())
                    print(grid)
                else:
                    continue

        return count

