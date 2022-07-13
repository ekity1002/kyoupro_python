N, Y = list(map(int, input().split()))

flag = False
for x in range(N, -1, -1):
    s = 10000*x
    if s>Y:
        continue
    if s==Y and x==N:
        print(f'{x} 0 0')
        flag = True
        break
    for y in range(N-x, -1, -1):
        s = 10000*x + 5000*y +(N-x-y)*1000
        if s > Y:
            continue
        if s==Y:
            print(f'{x} {y} {N-x-y}')
            flag=True
            break
    if flag:
        break
if not flag:
    print(f'-1 -1 -1')            
        