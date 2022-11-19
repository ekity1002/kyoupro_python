from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
# tmp = [0] * N
tmp = defaultdict(int)
AllVal = None
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        # Aのすべてに q1代
        AllVal = q[1]
        tmp = defaultdict(int)
    elif q[0] == 2:
        iq = q[1] - 1
        x = q[2]
        # A[iq] に x くわえる
        tmp[iq] += x
    elif q[0] == 3:
        iq = q[1] - 1
        if AllVal is None:
            # print("ans", A[iq] + tmp[iq])
            print(A[iq] + tmp[iq])
        else:
            print(AllVal + tmp[iq])
            # print("ans", AllVal + tmp[iq])
