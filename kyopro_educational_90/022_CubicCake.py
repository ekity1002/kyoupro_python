import math
A, B, C = list(map(int, input().split()))

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y,x%y)

g = gcd(A, gcd(B,C))

#print(g)
#g = math.gcd(A,math.gcd(B,C))
A, B, C = A//g, B//g, C//g

#print(A,B,C)

def check(edge):
    
    if edge==1:
        return 0
    else:
        return edge-1
e1, e2, e3 = check(A), check(B), check(C)

print(int(e1+e2+e3))
