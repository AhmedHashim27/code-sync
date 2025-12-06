class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        q = collections.deque()


        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        if fresh == 0:
            return 0


        mints = 0

        while q and fresh > 0:
            mints +=1

            for i in range(len(q)):
                r, c = q.popleft()

                directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                        continue 


                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -=1 
                        q.append((nr,nc))

        return mints if fresh == 0 else -1