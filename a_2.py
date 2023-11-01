# class Solution:
#     def loudAndRich(self, richer, quiet):
#         n = len(quiet)
#         graph = [[] for _ in range(n)]
#         for a, b in richer:
#             graph[b].append(a)
#
#         memo = [-1] * n
#
#         def dfs(node):
#             if memo[node] != -1:
#                 return memo[node]
#             memo[node] = node
#             for neighbor in graph[node]:
#                 candidate = dfs(neighbor)
#                 if quiet[candidate] < quiet[memo[node]]:
#                     memo[node] = candidate
#             return memo[node]
#
#         return [dfs(i) for i in range(n)]
#
#
# class Solution:
#     def catMouseGame(self, graph):
#         def getPreStates(m, c, t):
#             ans = []
#             if t == 1:
#                 for c2 in graph[c]:
#                     if c2 == 0: continue
#                     ans.append((m, c2, 2))
#             else:
#                 for m2 in graph[m]:
#                     ans.append((m2, c, 1))
#             return ans
#
#         def ifAllNextMovesFailed(m, c, t):
#             if t == 1:
#                 for m2 in graph[m]:
#                     if result[(m2, c, 2)] != 2: return False
#             else:
#                 for c2 in graph[c]:
#                     if c2 == 0: continue
#                     if result[(m, c2, 1)] != 1: return False
#             return True
#
#         result = defaultdict(lambda: 0)
#         n = len(graph)
#         queue = deque()
#
#         for t in range(1, 3):
#             for i in range(1, n):
#                 result[(0, i, t)] = 1
#                 queue.append((0, i, t))
#                 result[(i, i, t)] = 2
#                 queue.append((i, i, t))
#
#         while queue:
#             m, c, t = queue.popleft()
#             r = result[(m, c, t)]
#             for m2, c2, t2 in getPreStates(m, c, t):
#                 r2 = result[(m2, c2, t2)]
#                 if r2 > 0:
#                     continue
#                 if r == 3 - t:
#                     result[(m2, c2, t2)] = r
#                     queue.append((m2, c2, t2))
#                 elif ifAllNextMovesFailed(m2, c2, t2):
#                     result[(m2, c2, t2)] = 3 - t2
#                     queue.append((m2, c2, t2))
#         return result[(1, 2, 1)]
#
#
# class Solution:
#     def matrixRankTransform(self, matrix):
#         m = len(matrix);
#         n = len(matrix[0])
#
#         vals = defaultdict(list)
#         for i in range(m):
#             for j in range(n):
#                 vals[matrix[i][j]].append([i, j])
#
#         def find(i):
#             if i != parent[i]:
#                 parent[i] = find(parent[i])
#             return parent[i]
#
#         rank = [0] * (m + n)
#
#         for val in sorted(vals):
#             parent = list(range(m + n))
#
#             for i, j in vals[val]:
#                 p_i = find(i);
#                 p_j = find(j + m)
#                 parent[p_j] = p_i  # union
#                 rank[p_i] = max(rank[p_j], rank[p_i])
#
#             for i, j in vals[val]:
#                 matrix[i][j] = rank[find(i)] + 1
#
#             for i, j in vals[val]:
#                 rank[i] = rank[j + m] = matrix[i][j]
#
#         return matrix
#
# class Solution:
#     def sortItems(self, n, m, group, beforeItems):
#         for i in range(n):
#             if group[i]==-1:
#                 group[i]=i+m
#
#         graph0={}
#         seen0=[0]*(m+n)
#         graph1={}
#         seen1=[0]*n
#
#         for i,x in enumerate(beforeItems):
#             for j in x:
#                 if group[j]!=group[i]:
#                     graph0.setdefault(group[j],[]).append(group[i])
#                     seen0[group[i]]+=1
#
#                 graph1.setdefault(j,[]).append(i)
#                 seen1[i]+=1
#
#         def fn(graph,seen):
#             N=len(seen)
#             ans=[]
#             stack=[k for k in range(N) if seen[k]==0 ]
#             while stack:
#                 n=stack.pop()
#                 ans.append(n)
#                 for s in graph.get(n,[]):
#                     seen[s]-=1
#                     if seen[s]==0:
#                         stack.append(s)
#             return ans
#
#         top0=fn(graph0,seen0)
#         a=len(top0)
#         b=len(seen0)
#         if a!=b:
#             return []
#
#         top1=fn(graph1,seen1)
#         c=len(top1)
#         d=len(seen1)
#         if c!=d:
#             return []
#         map0={x:i for i,x in enumerate(top0)}
#         map1={x:i for i,x in enumerate(top1)}
#         return sorted( range(n),key=lambda x:(map0[group[x]],map1[x]))
#
#
# import math
#
#
# class Solution:
#     def waysToBuildRooms(self, p):
#         def aux(l):
#             sum_l = sum(l)
#             l.sort(reverse=True)
#             i = l[0]
#             a = 1
#             for j in range(1, len(l)):
#                 for k in range(l[j]):
#                     a *= (i + k + 1)
#                 a = a // math.factorial(l[j])
#                 i += l[j]
#                 a = a % (10 ** 9 + 7)
#             return a
#
#         n = len(p)
#         if n == 2:
#             return 1
#         d_chil = {}
#         for i in range(1, n):
#             if p[i] in d_chil.keys():
#                 d_chil[p[i]] += [i]
#             else:
#                 d_chil[p[i]] = [i]
#
#         d_n_chil = {}
#
#         def find_n_chil(idx):
#             if idx not in d_chil.keys():
#                 d_n_chil[idx] = 1
#                 return 1
#             a = 0
#             for i in range(len(d_chil[idx])):
#                 a += find_n_chil(d_chil[idx][i])
#             d_n_chil[idx] = a + 1
#             return a + 1
#
#         find_n_chil(0)
#
#         def count_ways(idx):
#             if idx not in d_chil.keys():
#                 return 1
#             l = d_chil[idx]
#             if len(l) == 1:
#                 return count_ways(l[0])
#             else:
#                 a = 1
#                 s = []
#                 for i in l:
#                     a *= count_ways(i)
#                     a = a % (10 ** 9 + 7)
#                     s += [d_n_chil[i]]
#                 a *= aux(s)
#                 return a % (10 ** 9 + 7)
#
#         return count_ways(0)