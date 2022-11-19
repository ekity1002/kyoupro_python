H, M = map(int, input().split())


def isvalid(h, m):
    return 0 <= h <= 23 and 0 <= m <= 59


def change_time(h, m):
    if 0 <= h <= 9:
        A = "0"
        B = str(h)
    else:
        A = str(h)[0]
        B = str(h)[1]
    if 0 <= m <= 9:
        C = "0"
        D = str(m)
    else:
        C = str(m)[0]
        D = str(m)[1]
    new_h = int(A + C)
    new_m = int(B + D)
    # print("cnange_time", new_h, new_m)
    return new_h, new_m


def update(h, m):
    # 1分進める
    new_m = m + 1
    new_h = h
    if new_m > 59:
        new_m = 0
        new_h = h + 1
    if new_h > 23:
        new_h = 0

    return new_h, new_m


while True:
    # print("H,M", H, M)
    new_h, new_m = change_time(H, M)
    if isvalid(new_h, new_m):
        print(H, M)
        break
    H, M = update(H, M)
