class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def calculateP(r,c,grid):
            count = 0
            pairs = [[-1,0],[1,0],[0,1],[0,-1]]
            for x,y in pairs:
                new_r = x+r
                new_c = y+c

                if new_r<0:
                    count+=1
                elif new_r==len(grid):
                    count+=1
                # elif new_r == 0:
                #     count+=1
                elif new_c<0:
                    count+=1
                elif new_c==len(grid[0]):
                    count+=1
                elif grid[new_r][new_c] == 0:
                    count+=1
                # print(r,c,new_r,new_c,count)
            # grid[r][c]=count
            return count
        ans =0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    ans += calculateP(r,c,grid)
        return ans
