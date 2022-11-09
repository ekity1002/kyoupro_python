#
# Typical90 / 029 - Long Bricks（★5）
#
# https://atcoder.jp/contests/typical90/tasks/typical90_ac

# tag: segment tree with lazy propagation
# セグメント木
# https://algo-logic.info/segment-tree/
# ---------------------------------------------------------------------------- #

from time import process_time
import sys

sys.setrecursionlimit(10**9)

# ---------------------------------------------------------------------------- #
class SegmentTreeLazy:
    # [ constructor ]
    def __init__(self, n: int) -> None:
        # < set element count / identify element >
        self._n = n  # 最大幅
        self._e = -1

        # < set segment size >
        size = 1
        while size < n + 1:
            size *= 2
        self._size = size
        # < set segment value >
        self._segs = [0] * (self._size * 2)  # 高さを格納
        self._lazy = [-1] * (self._size * 2)

    # [ propagation ]
    def _propagation(self, pos):
        self._lazy[pos * 2] = self._lazy[pos]
        self._lazy[pos * 2 + 1] = self._lazy[pos]
        self._lazy[pos] = self._e

    # [ update ]
    def _update(self, x):
        self._segs[x] = max(self._segs[x], self._lazy[x])

    # [ getMax ]
    def getMax(self, L, R):
        """L, R,間の最大値を返す

        Args:
            L (_type_): _description_
            R (_type_): _description_

        Returns:
            _type_: _description_
        """
        return self._getMax(L, R, 0, self._size, 1)

    def _getMax(self, L, R, l, r, pos):
        """_summary_

        Args:
            L (_type_): _description_
            R (_type_): _description_
            l (_type_): 左端
            r (_type_): 右端
            pos (_type_): _description_

        Returns:
            _type_: _description_
        """
        # in range ?
        if L <= l and r <= R:
            # 長方形が最大、最小区間を含んでいる
            return self._segs[pos]
        if r <= L or R <= l:
            # 長方形が範囲外
            return 0

        # need update ?
        if self._lazy[pos] != self._e:
            # propagate lazy
            self._propagation(pos)
            # update segs
            self._update(pos * 2)
            self._update(pos * 2 + 1)

        # move next
        m = (l + r) // 2
        maxL = self._getMax(L, R, l, m, pos * 2)
        maxR = self._getMax(L, R, m, r, pos * 2 + 1)
        maxLR = max(maxL, maxR)
        return maxLR

    # [ setMax ]
    def setMax(self, L, R, val):
        self._setMax(L, R, val, 0, self._size, 1)

    def _setMax(self, L, R, val, l, r, pos):
        # in range ?
        if L <= l and r <= R:
            self._lazy[pos] = val
            self._update(pos)
            return
        if r <= L or R <= l:
            return
        # need update ?
        if self._lazy[pos] != self._e:
            # propagate lazy
            self._propagation(pos)
            # update segs
            self._update(pos * 2)
            self._update(pos * 2 + 1)
        # move next
        m = (l + r) // 2
        self._setMax(L, R, val, l, m, pos * 2)
        self._setMax(L, R, val, m, r, pos * 2 + 1)
        self._segs[pos] = max(
            self._segs[pos], self._segs[pos * 2], self._segs[pos * 2 + 1]
        )


from pdb import set_trace as st


def solve():
    W, N = map(int, input().split())
    # st()

    stree = SegmentTreeLazy(W)
    ans = []
    for i in range(N):
        l, r = map(int, input().split())
        nowH = stree.getMax(l, r + 1) + 1
        ans.append(nowH)
        # print(nowH)
        stree.setMax(l, r + 1, nowH)
    [print(h) for h in ans]


solve()
