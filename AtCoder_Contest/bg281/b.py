import string

S = input()
if len(S) != 8:
    print("No")
    exit(0)

if S[0] not in string.ascii_uppercase or S[-1] not in string.ascii_uppercase:
    print("No")
    exit(0)

try:
    a = int(S[1:-1])
    if 100000 <= a <= 999999:
        print("Yes")
    else:
        print("No")
except:
    print("No")
