from itertools import combinations as combo


def sieve(n):
    "Return all primes <= n."
    np1=n+1
    s=(range(np1))  # leave off `list()` in Python 2
    s[1]=0
    sqrtn=int(round(n**0.5))
    for i in xrange(2, sqrtn+1):  # use `xrange()` in Python 2
        if s[i]:
            # next line:  use `xrange()` in Python 2
            s[i*i: np1: i]=[0]*len(range(i*i, np1, i))
    return [x for x in s if x]

from fractions import gcd

for _ in range(input()):
    N=input()
    A=map(int, raw_input().split())
    if 1 in A: print "YES"
    elif N == 1: print "NO"
    else:
        if reduce(gcd, A)==1:
            print "YES"
        else: print "NO"



        # found="NO"
        # for x in range(2, N+1):
        #     for B in combo(A, x):
        #         # print B
        #         if not any([integer for integer in sieve(max(B)) if not any([a%integer for a in B])]):
        #             found="YES"
        #             break
        #             # print found
        # print found