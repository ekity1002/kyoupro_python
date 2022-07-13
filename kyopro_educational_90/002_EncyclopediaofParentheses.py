# https://drken1215.hatenablog.com/entry/2021/06/12/151200
from itertools import product

def is_valid(s):
    score=0
    for c in s:
        if c=='(':
            score+=1
        else:
            score-=1
            
        if score < 0:
            return False
    return (score==0)

N = int(input())

for s in product(['(' , ')'], repeat=N):
    if is_valid(s):
        print(*s, sep='')
