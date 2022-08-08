A = [[0] * 4 for _ in range(4)]
A[0] = list(map(int, input().split()))

#print(A)
for i in range(1,4):
    for j in range(0,4):
        # まうえ
        A[i][j] += A[i-1][j]

        # 右上
        if j!=3:
            A[i][j] += A[i-1][j+1]

        #左上
        if j!=0:
            A[i][j] += A[i-1][j-1]
print(A[3][3])