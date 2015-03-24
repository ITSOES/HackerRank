def sum_subarray(L):
    csum=best=None
    for l in L:
        csum = csum+l if csum > 0 else l
        best=max(best, csum)
    return best
for _ in xrange(input()):
    input()
    L=[int(x) for x in raw_input().split()]
    cont = sum_subarray(L)
    print cont, sum(x for x in L if x > 0) if cont>0 else cont