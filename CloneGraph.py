#133. Clone Graph
#Given a reference of a node in a connected undirected graph. Return a deep copy (clone) of the graph.

class Node():
    def __init__(self,val):
        self.val=val
        self.neighbors=None

class Graph():
    def clonegraph(self,node):
        oldtonew={}

        def dfs(node):
            if(node in oldtonew):
                return(oldtonew[node])
            copy= Node(node.val)
            oldtonew[node]=copy
            for nei in node.neighbors:
                copy.neighbors.append((nei))
            return(copy)

        return(dfs(node)) if node else None
