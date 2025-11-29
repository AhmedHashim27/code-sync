class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """


        preMap = {i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visited = set()
        visiting = set()

        def dfs(crs):
            if crs in visiting:
                return False
            if crs in visited:
                return True
            
            visiting.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            visiting.remove(crs)
            visited.add(crs)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True  


        # inEdgeCount = [0] * numCourses
        # nxtCourses = defaultdict(list)
        # for pre in prerequisites:
        #     inEdgeCount[pre[0]] += 1
        #     nxtCourses[pre[1]].append(pre[0])
        # # find course without prerequisite
        # queue = deque()
        # for course, count in enumerate(inEdgeCount):
        #     if count == 0:
        #         queue.append(course)
        # # remove inEdges
        # takenCourse = len(queue)
        # while queue:
        #     course = queue.popleft()
        #     for adj in nxtCourses[course]:
        #         inEdgeCount[adj] -= 1
        #         if inEdgeCount[adj] == 0:
        #             queue.append(adj)
        #             takenCourse += 1
        # return takenCourse == numCourses