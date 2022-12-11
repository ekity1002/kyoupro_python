from collections import defaultdict

N = int(input())
S = []
d = defaultdict(list)
for i in range(N):
    s = input()
    S.append((ord(s[0]) - ord("a"), ord(s[-1]) - ord("a")))

# (先頭の文字の整数index, あとの文字の整数index)
# a=0, b=1, ...
cnt = 2**N
dp = [0] * cnt
for s in range(1, cnt):
    for c in range(
        N,
    ):
        # 計算の優先順位：シフト演算後, & とられる
        # s を c bit シフトして、最下位ビットが1か？
        if 1 & s >> c:
            print(s, c)
            # 1を cbit左シフト, sと  xor -> sのcビット目を反転
            # dp not した数だけ、 S[c][1] を 右シフトし、最下位ビットを取り出す
            # s[c][0]だけ左シフト = tmp
            # dp[s] tmp orして格納
            # s = 1,2,3,...2**N
            # c = 0,1,2,,,N
            tmp = (1 & ~dp[s ^ 1 << c] >> S[c][1]) << S[c][0]
            dp[s] = dp[s] | tmp

print("First" if dp[-1] else "Second")
