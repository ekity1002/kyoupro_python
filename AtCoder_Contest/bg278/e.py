from collections import defaultdict

N = int(input())
S = []
d = defaultdict(list)
for i in range(N):
    s = input()
    S.append(s)
    d[s[0]] = i


def game(i):
    word = S[i]
    turn = "First"  # 先行
    st = [word]
    cnt = 0
    checked = set(["word"])
    while st:
        word = st.pop()
        word_id_kouho = d[word[-1]]
        for i in word_id_kouho:
            if S[i] not in checked:
                checked.add(S[i])
                st.append(S[i])
        pass
    return cnt, turn


cnt = 0
ans = "First"
for i in range(N):
    # ゲームスタート
    tmp, turn = game(i)
    if cnt < tmp:
        cnt = tmp
        ans = turn
print(ans)
