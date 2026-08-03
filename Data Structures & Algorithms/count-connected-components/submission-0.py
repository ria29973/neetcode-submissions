class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        adj = [[] for i in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def bfs(node):
            q = [node]
            visited.add(node)
            while q:
                e = q.pop(0)
                for nei in adj[e]:
                    if nei not in visited:
                        q.append(nei)
                        visited.add(nei)
        
        components = 0
        for i in range(n):
            if i not in visited:
                components+=1
                bfs(i)
        return components

                
                

                



        