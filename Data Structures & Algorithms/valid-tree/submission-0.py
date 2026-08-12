class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = set()
        def dfs(v, par):
            if v in visited:
                return False
            visited.add(v)
            for u in adj[v]:
                if u == par:
                    continue
                if not dfs(u, v):
                    return False
            return True
        
        if not dfs(0, -1):
            return False
        return len(visited) == n

        