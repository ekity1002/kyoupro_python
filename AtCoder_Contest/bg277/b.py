N = int(input())
ans = "Yes"
s_dict = {}
for i in range(N):
    s = input()
    if not s[0] in ["H", "D", "C", "S"]:
        ans = "No"
    if not s[1] in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]:
        ans = "No"
    if s_dict.get(s) == True:
        ans = "No"

    s_dict[s] = True
print(ans)
