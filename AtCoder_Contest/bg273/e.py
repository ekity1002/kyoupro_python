from collections import deque
from collections import defaultdict

Q = int(input())
G = [[0, -1, -1]]  # (前のindex, 値, 次index)
NOTE = defaultdict(int)
current = 0
ans = []
for i in range(Q):
    q = input().split()
    if q[0] == "ADD":
        # ついか
        prev, val, next = G[current]

        G.append([current, int(q[1]), -1])

        G[current] = [prev, val, len(G) - 1]

        current = len(G) - 1
    elif q[0] == "SAVE":
        NOTE[int(q[1])] = current
    elif q[0] == "DELETE":
        prev, val, next = G[current]

        p_prev, p_val, p_next = G[prev]

        G[prev] = [p_prev, p_val, -1]

        current = prev

    elif q[0] == "LOAD":
        current = NOTE[int(q[1])]
    ans.append(G[current][1])

print(*ans)
