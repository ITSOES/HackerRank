from math import ceil
N=input()
X=[input() for _ in range(N)]
print 'X', X
l=[]

# for i, n in enumerate(d):
#     appended=False
#     print n
#     for t in l:
#         if n > t[-1]:
#             t.append(n)
#             appended=True
#     if not appended: l.append([n])
# print max(len(y) for y in l)
# print l
# print d


P=[0]*(N)
M=[None]*(N+1)

L=lo=mid=0
for i in range(N):
    print
    print 'M', M
    print 'P', P
    lo=1
    hi=L
    while lo<=hi:
        mid=int(ceil((lo+hi)/2.))
        print '   ',X[M[mid]] , X[i]

        if X[M[mid]] < X[i]:
            lo=mid+1
        else:
            hi=mid-1


    newL=lo
    print 'i',i, 'mid', mid, 'lo hi', (lo,hi)

    P[i]=M[newL-1]
    M[newL]=i

    if newL > L:
        L=newL
print X, P, M
print L
# //Reconstruct the longest increasing subsequence
S=[None]*L
k=M[L]
for i in xrange(L-1, -1,-1):
    S[i]= X[k]
    k   = P[k]

print S