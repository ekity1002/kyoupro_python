import string

N, K = map(int, input().split())
S = input()
chars = list(string.ascii_lowercase)

from pdb import set_trace as st

def calc_next(S):
    """# res[i][c] := i 文字目以降で最初に文字 c が登場する index
    存在しないときは N
    """    
    N = len(S)
    nex = [[N]*26 for _ in range(N+1)]

    for i in range(N-1, -1, -1):
        for j in range(26):
            nex[i][j] = nex[i+1][j]
        nex[i][ord(S[i]) - ord('a')] = i

    return nex
        


res = ''
nex = calc_next(S)

j = -1
for i in range(K):
    for ordc in range(26):
        k = nex[j+1][ordc] #文字列Sのj+1番目の文字より先にある a-zの文字の位置

        # k-i： i番目の文字から 次に小さいアルファベットまでの距離
        if N-k >= k-i:
            res += chr(ord('a') + ordc)
            j=k
            break
        
print(nex)