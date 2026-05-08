class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        ROW = len(grid)
        COL = len(grid[0])
        vists = []
        for r in range(ROW):
            vists.append([False]*COL)
        q = deque()

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    q.append((r,c))
                    

        def checkBfs(r,c,grid):
            if min(r,c)<0 or r>= ROW or c >= COL or grid[r][c]<1 or vists[r][c]==True:
                return 
            q.append((r,c))
            vists[r][c]=True
            
        level =0
        while q:
           
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c]=level

                checkBfs(r-1,c,grid)
                checkBfs(r+1,c,grid)
                checkBfs(r,c-1,grid)
                checkBfs(r,c+1,grid)
             
                

            level+=1


        