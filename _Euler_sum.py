
primes = [1,2,3,5,7,11,13,17,19,23] #+ [0,0,0,4]


def f(x):
    # return float(primes[x] + x)
    return float(-9**x*5) + 900

def euleridentity(f, x):
    n1, n2 = (f(x)), f(x - 1) #if x>1 else 1/float(1)
    result = (n1 - n2) /float(n1 * n2)
    print('n1 n2', n1, n2, n1 * n2, result)
    return result
    return 1/float(n2) - 1/float(n1)

def eulersum(f,a,n=1):
    return reduce(lambda r, i: r + f(i), range(n, a + 1), 0)

from functools import partial

pei = partial(partial,euleridentity)
eif = partial(euleridentity,f)
f_2 = f #lambda x: f(f(x)) + 90
a = 4  #len(primes)-1
b = 1
ps = eulersum(pei(f_2),a, b)
ps2 = 1./(float(f_2(a)) or 1)
print ps,ps2,(f(a)-1)/f(a)
print ps+ps2, 1/float(f_2(b-1))

from time import time

t= time()

def factorialmod(x, mod=0):
    result = 1
    if not mod:
        mod = x
        x-=1
    for n in xrange(1,x):
        result *= n
        result %= mod
    return result
t= time()-t

print

print 'fact', factorialmod(1031)

print 'clock', t