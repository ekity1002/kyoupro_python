N = int(input())
schedules = [list(map(int, input().split())) for _ in range(N)]
#print(schedules)

schedules.sort(key=lambda x: x[1])
#print(schedules)

prev_end = schedules[0][1]
ans = 1
for i in range(1, N):
    if prev_end <= schedules[i][0]:
        ans+=1       
        prev_end = schedules[i][1]
print(ans)