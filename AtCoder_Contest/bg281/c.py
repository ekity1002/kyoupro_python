N, T = map(int, input().split())
A = list(map(int, input().split()))

T = T % sum(A)

# T病後
# どの曲,  その曲のなんびょうめ？
sum_t = 0
for i, a in enumerate(A):
    tmp_sum_t = sum_t + a
    # print(sum_t, tmp_sum_t)
    if T < tmp_sum_t:
        print(f"{i+1} {T-sum_t}")
        break
    sum_t = tmp_sum_t
