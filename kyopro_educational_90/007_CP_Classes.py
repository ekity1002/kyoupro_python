from bisect import bisect_left

N = int(input())
A = list(map(int, input().split())) #rating
Q = int(input())
A.sort()

# def f(x, b):
#     return b <= A[x]


for _ in range(Q):
    b = int(input())
    # left = 0
    # right = N
    #st()
    # while abs(right-left) >=1:
    #     mid = (left+right)//2
    #     if f(mid, b):
    #         right = mid
    #     else:
    #         left = mid + 1
    # #print('@@@@@', left, right)    
    j = bisect_left(A, b)
    ans = 1e10
    if j < N:
        ans = min(ans, abs(b - A[j]))
    if 0 < j:
        # 切り上げで返されるので, 0より大きい場合は 一つ小さい添字とも比較
        ans = min(ans, abs(A[j-1] - b))

    print(ans)