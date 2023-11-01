# class Solution:
#     def canFinish(self, numCourses, prerequisites):
#         graph = [[] for _ in range(numCourses)]
#         for u, v in prerequisites:
#             graph[u].append(v)
#
#         visited = [0] * numCourses
#
#         def dfs(node):
#             if visited[node] == -1:
#                 return False
#
#             if visited[node] == 1:
#                 return True
#
#             visited[node] = -1
#
#             for neighbor in graph[node]:
#                 if not dfs(neighbor):
#                     return False
#
#             visited[node] = 1
#
#             return True
#
#         for i in range(numCourses):
#             if not dfs(i):
#                 return False
#
#         return True
#
#
# class Solution:
#     def findOrder(self, numCourses, prerequisites):
#         graph = defaultdict(list)
#         in_degree = [0] * numCourses
#         for course, pre in prerequisites:
#             graph[pre].append(course)
#             in_degree[course] += 1
#
#         queue = deque()
#         for i in range(numCourses):
#             if in_degree[i] == 0:
#                 queue.append(i)
#
#         order = []
#         while queue:
#             curr = queue.popleft()
#             order.append(curr)
#             numCourses -= 1
#             for neighbor in graph[curr]:
#                 in_degree[neighbor] -= 1
#                 if in_degree[neighbor] == 0:
#                     queue.append(neighbor)
#
#         if numCourses == 0:
#             return order
#         else:
#             return []

# class Solution(object):
#     def findMinHeightTrees(self, n, edges):
#         if n == 1:
#             return [0]
#         adj = [[] for _ in range(n)]
#         for a, b in edges:
#             adj[a].append(b)
#             adj[b].append(a)
#         leaves = [i for i in range(n) if len(adj[i]) == 1]
#         while n > 2:
#             n -= len(leaves)
#             new_leaves = []
#             for leaf in leaves:
#                 neighbor = adj[leaf][0]
#                 adj[neighbor].remove(leaf)
#                 if len(adj[neighbor]) == 1:
#                     new_leaves.append(neighbor)
#             leaves = new_leaves
#         return leaves
#
#
# class Solution:
#     def longestIncreasingPath(self, matrix):
#         if not matrix:
#             return 0
#         m, n = len(matrix), len(matrix[0])
#         memo = [[0] * n for _ in range(m)]
#         directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
#
#         def dfs(i, j):
#             if memo[i][j]:
#                 return memo[i][j]
#             res = 1
#             for dx, dy in directions:
#                 x, y = i + dx, j + dy
#                 if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
#                     res = max(res, dfs(x, y) + 1)
#             memo[i][j] = res
#             return res
#
#         ans = 0
#         for i in range(m):
#             for j in range(n):
#                 ans = max(ans, dfs(i, j))
#         return ans
#
#
# class Solution(object):
#     def eventualSafeNodes(self, graph):
#         n = len(graph)
#         status = [0] * n
#
#         def dfs(node):
#             if status[node] != 0:
#                 return status[node] == 1
#             status[node] = 2
#             for neighbor in graph[node]:
#                 if not dfs(neighbor):
#                     return False
#             status[node] = 1
#             return True
#
#         safe_nodes = []
#         for i in range(n):
#             if dfs(i):
#                 safe_nodes.append(i)
#         return safe_nodes