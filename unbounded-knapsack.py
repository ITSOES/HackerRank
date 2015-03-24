import sys
from itertools import ifilter
from time import time


c1=time()


def multisum(k, C):
    D={0: True}
    for i in xrange(1, k+1):
        if any(i-c in D for c in C): D[i]=True
        for c in C:
            if i-c in D: D[i]=True;break
    print max(D)


T=int(raw_input())
for i in range(T):
    n, k=map(int, raw_input().split())
    C=set(map(int, raw_input().split()))
    multisum(k, C)

c1=time()-c1



############# MINE (c2) #####################

c2=time()


def gcd(a, b):
    while b:
        a, b=b, a%b
    return a


sp=lambda: map(int, raw_input().split())


def getbest(k, a):
    bests={k}
    for c in a:
        if 0 in bests: return k, bests
        bests.update(*(range(e-c, -1, -c) for e in bests))
    return (k-min(bests)), bests


for _ in xrange(input()):
    k=sp()[1]
    a=set(sp())
    # k1=k%(reduce(lambda x, y: x*y/gcd(x, y), a)) # this optimizes for larger k:avg(a) values
    bests={k}

    print getbest(k, a)

test, bests = getbest(590, [2, 17, 47, 89])
print 'test', test, len(bests), bests, divmod(57, 17)
c2=time()-c2
############# END of Mine ########
c3=time()

T=int(sys.stdin.readline())


def findMultsum(ar, k, cur=0, index=0):
    if index >= len(ar): return cur

    best=0

    # cur=start
    while cur <= k:
        newsum=findMultsum(ar, k, cur, index+1)
        if newsum == k: return k
        if newsum > best:
            best=newsum
        cur+=ar[index]

    return best


for t in xrange(T):
    N, k=[int(x) for x in sys.stdin.readline().split()]
    ar=[int(x) for x in sys.stdin.readline().split()]
    # if len(ar) != N:
    # raise RuntimeError, "malformed input"
    ar=list(set(ar))

    print findMultsum(ar, k)

c3=time()-c3

c4=time()
tcn=int(raw_input())

for tc in xrange(0, tcn):
    n, k=map(int, raw_input().split())
    coins=set(map(int, raw_input().split()))
    marked={0: True}
    for i in xrange(1, k+1):
        for coin in coins:
            if i-coin in marked:
                marked[i]=True
                break

    print max(marked)
c4=time()-c4

print 'clock1', c1, 'clock2', c2, 'clock3', c3, 'clock4', c4