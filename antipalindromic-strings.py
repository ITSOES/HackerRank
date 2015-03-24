p =(10**9+7)
for _ in xrange(input()):
    n, m=map(int, raw_input().split())
    print( (m*(m-1)*pow((m-2),(n-2), p)) if n > 2 else m if n == 1 else (m*(m-1)))%p