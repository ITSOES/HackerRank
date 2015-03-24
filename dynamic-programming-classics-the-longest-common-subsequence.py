from pprint import pprint as pp
from numpy import *

sp=lambda: raw_input().split()
n, m=map(int, sp())
a, b=sp(), sp()
# if len(a)>len(b):a,b=b,a


def lcs(a, b, n=n, m=m):
    # lengths=[[0]*(m+1) for i in range(n+1)]
    # lengths = array([[0]*(len(b)+1)]*(len(a)+1))
    lengths = zeros((n+1,m+1), int)
    # row 0 and column 0 are initialized to 0 already
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                lengths[i+1][j+1]=lengths[i][j]+1
            else:
                lengths[i+1][j+1]= max(lengths[i+1][j], lengths[i][j+1])
    # read the substring out from the matrix
    result = []
    # n, m =len(a), len(b)
    # pp(lengths)
    print lengths
    while n != 0 and m != 0:
        if lengths[n][m] == lengths[n-1][m]:
            n-= 1
        elif lengths[n][m] == lengths[n][m-1]:
            m-= 1
        else:
            assert a[n-1] == b[m-1]
            result = [a[n-1]]+result
            n-=1
            m-=1
    return result


print ' '.join(lcs(a, b))