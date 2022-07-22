from pdb import set_trace as st
H, W = map(int, input().split())
G = [None for _ in range(H*W)]
grid = [[0 for _ in range(W)] for _ in range(H)]
seen = [False for _ in range(H*W)]

for h in range(H):
    for i, s in enumerate(input()):
        if s == '.':
            grid[h][i] = 0
        else:
            grid[h][i] = 1

#print(grid)
#print(seen)

def getidx(h,w,direction):
    nh, nw= h, w
    if direction == 'up':
        nh = h-1
    elif direction == 'down':
        nh = h+1
    elif direction == 'left':
        nw = w-1
    elif direction == 'right':
        nw = w+1
    return nh, nw


def isvalid(h,w):
    """
    h,w: 現在のh,w
    direction: 取得するgrid方向
    """
    if h < 0 or w < 0 or h > H-1 or w > W-1:
        return False
    return True


# Gをさくせい
for h in range(H):
    for w in range(W):
        if grid[h][w] == 0:
            continue
        G[h*W + w] = []
        #st()
        nh, nw = getidx(h,w,'up')
        if isvalid(nh, nw) and grid[nh][nw] == 1:
            G[h*W + w].append(nh*W + nw)
        nh, nw = getidx(h,w,'down')
        if isvalid(nh, nw) and grid[nh][nw] == 1:
            G[h*W + w].append(nh*W + nw)
        nh, nw = getidx(h,w,'left')
        if isvalid(nh, nw) and grid[nh][nw] == 1:
            G[h*W + w].append(nh*W + nw)
        nh, nw = getidx(h,w,'right')
        if isvalid(nh, nw) and grid[nh][nw] == 1:
            G[h*W + w].append(nh*W + nw)
            
#print(G)

def dfs(s):
    dist = [-1] * (H*W)
    dist[s] = 0
    seen[s] = True

    st = [s]
    while st:
        v = st.pop()
        for nv in G[v]:
            if dist[nv] == -1:
                seen[nv]=True
                dist[nv] = dist[v]+1
                st.append(nv)

    return dist

ans = 0
for i in range(H*W):
    if seen[i]:
        continue
    if G[i] is None:
        continue
    dfs(i)
    ans+=1
print(ans)
