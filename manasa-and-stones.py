for _ in range(input()):
    n, a, b=input(), input(), input()
    if a==b: print n*a-b  # edge case
    else:    print ' '.join([str(a*(n-1-c)+b*c) # Effective as combination_with_replacement()
                                 for c in range(n)[::cmp(b, a)]])

# # Alternate Solution
# from itertools import combinations_with_replacement as product
# for _ in range(input()):
#     n, ab=input(), sorted([input(), input()])
#     result=[str(sum(x)) for x in product(ab, n-1)]
#     print ' '.join(result)