# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = [[False, None] for _ in range(101)]

        def dfs(raw_node: 'Node'):
            if raw_node is None:
                return None
            clone_node = Node(raw_node.val)
            visited[raw_node.val] = [True, clone_node]
            for node in raw_node.neighbors:
                if visited[node.val][0]:
                    clone_node.neighbors.append(visited[node.val][1])
                else:
                    clone_node.neighbors.append(dfs(node))
            return clone_node

        return dfs(node)


class Solution:
    def __init__(self):
        self.visited = dict()

    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        clone_node = Node(node.val)
        self.visited[node] = clone_node
        for neighbor in node.neighbors:
            if neighbor in self.visited:
                clone_node.neighbors.append(self.visited[neighbor])
            else:
                clone_node.neighbors.append(self.cloneGraph(neighbor))
        return clone_node
