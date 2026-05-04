class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:

        def dfs(grid,r,c,visits):
            ROWS, COLS= len(grid), len(grid[0])

            if (min(r,c)<0 or r ==ROWS 
            or c ==COLS or (r,c) in visits or grid[r][c]==1):
                return 0

            if r ==ROWS-1 and c ==COLS-1:
                return 1

            count = 0
            visits.add((r,c))
            count+=dfs(grid,r-1,c,visits)
            count+=dfs(grid,r+1,c,visits)
            count+=dfs(grid,r,c+1,visits)
            count+=dfs(grid,r,c-1,visits)
            visits.remove((r,c))

            return count
        return dfs(grid,0,0,set())
