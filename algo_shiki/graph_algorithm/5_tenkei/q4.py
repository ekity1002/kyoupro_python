# import sys
# sys.setrecursionlimit(10**6)

# N, M = map(int, input().split())
# G = [[] for _ in range(N)]
# for _ in range(M):
#     a,b = map(int, input().split())
#     G[a].append(b)
#     G[b].append(a)


# seen = [-1] * N

# from pdb import set_trace as sst
# def dfs(s):
#     dist = [[-1, -1]]*N
#     dist[s] =[0, True] # 距離、色(0 or 1)

#     st = [s]
#     #sst()
#     while st:
#         v = st.pop()
#         seen[v] = True
#         for nv in G[v]:
#             if dist[nv][0] == -1:
#                 dist[nv] = [dist[v][0]+1, (not dist[v][1])]
#                 st.append(nv)
#             if dist[nv][1] == dist[v][1]:
#                 return False
#             if not dfs(nv):
#                 return False
#     return True

# #print(G)
# flg = True
# for n in range(N):
#     if seen[n]:
#         continue

#     if not dfs(n):
#         flg = False
#         break
    
# if flg:
#     print('Yes')
# else:
#     print('No')

import sys
sys.setrecursionlimit(10**6)

# 頂点 v を始点とした深さ優先探索
def dfs(v, G, color):
    # G[v] に含まれる頂点 v2 について、
    for v2 in G[v]:
        # v2 がすでに探索済みならば、スキップする
        if color[v2] != -1:
            # 隣り合う頂点どうしが同じ色なら、答えは No
            if color[v2] == color[v]: return False
            continue
        # そうでなければ、頂点 v2 の色を color[v] と逆にしたうえで
        # v2 始点で深さ優先探索を行う (関数を再帰させる)
        color[v2] = 1 - color[v]
        if not dfs(v2, G, color): return False
    return True

# main
# 入力を受け取る
N, M = map(int, input().split())
G = [[] for _ in range(N)]  # グラフを表現する隣接リスト
for i in range(M):
    a, b = map(int, input().split())
    # 頂点 a から頂点 b への辺を張る
    G[a].append(b)
    # 無向グラフのため、頂点 b から頂点 a への辺も張る
    G[b].append(a)

color = [-1 for _ in range(N)]    # color[v]：頂点 v の色が黒なら 1, 白なら 0, 未探索なら -1
ans = 'Yes'
# 全ての頂点について
for v in range(N):
    # 頂点 v がすでに訪問済みであれば、スキップ
    if color[v] != -1: continue
    # そうでなければ、頂点 v を含む連結成分は未探索
    # 頂点 v の色を白で決め打ちしたうえで、深さ優先探索を行う
    color[v] = 1
    if not dfs(v, G, color): ans = 'No'
# 答えを出力する
print(ans)