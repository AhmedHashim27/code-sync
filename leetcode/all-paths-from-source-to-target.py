class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """

        target = len(graph) - 1
        results = []
        

        def backtrack(current_node, current_path):
            if current_node == target:

                results.append(current_path[:])
                return

            for neighbor in graph[current_node]:
                current_path.append(neighbor)
                
                backtrack(neighbor, current_path)
                

                current_path.pop()

        backtrack(0, [0])
        
        return results