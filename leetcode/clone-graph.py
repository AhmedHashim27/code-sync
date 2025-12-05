"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        new = {}



        def dfs(node):
            if not node:
                return None
            if node in new:
                return new[node]

            copy = Node(node.val)
            new[node] = copy

            for n in node.neighbors:
                copy.neighbors.append(dfs(n))

            return copy
        return dfs(node)



    #     if node is None:
    #         return node
    #     clones=dict()
    #     return self.recurse(node,clones)
    
    # def recurse(self, node, clones):
    #     clone = Node(node.val)
    #     clones[node.val] = clone
    #     newNb = []
    #     for n in node.neighbors:
    #         if n.val not in clones:
    #             self.recurse(n, clones)
    #         newNb.append(clones[n.val])
    #     clone.neighbors = newNb
    #     return clone