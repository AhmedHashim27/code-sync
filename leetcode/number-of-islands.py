class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        if not grid:
            return 0

        rows , cols = len(grid), len(grid[0])
        island = 0

        def dfs(r,c):
            if r < 0 or c <0 or r >= rows or c >= cols or grid[r][c] == "0":
                return 

            grid[r][c] = "0"


            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    island += 1

                    dfs(r,c)
        return island








        # rows , cols = len(grid), len(grid[0])
        # visited = set()
        # island = 0 

        # def bfs(r,c):
        #     q = collections.deque()
        #     visited.add((r,c))
        #     q.append((r,c))

        #     while q:
        #         row , col = q.popleft()
        #         directions = [[1,0],[-1,0],[0,1],[0,-1]]

        #         for dr, dc in directions:
        #             r , c = row + dr , col + dc
        #             if (r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r,c) not in visited):
        #                 q.append((r,c))
        #                 visited.add((r,c))
                        
        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == "1" and (r,c) not in visited:
        #             bfs(r,c)
        #             island +=1 
        # return island