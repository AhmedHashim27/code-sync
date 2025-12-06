from collections import deque
class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """

        if not rooms:
            return 

        rows, cols = len(rooms), len(rooms[0])

        q = collections.deque()

        inf = 2147483647

        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    q.append((r,c))

        while q:
            r, c = q.popleft()

            directions = [(1,0),(0, -1),(0,1),(-1,0)]

            for dr, dc in directions:
                nr = dr + r
                nc = dc + c

                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue 


                if rooms[nr][nc] != inf:
                    continue 

                rooms[nr][nc] = rooms[r][c] + 1

                q.append((nr, nc))