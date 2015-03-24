from collections import defaultdict, Counter
sp=lambda: map(int, raw_input().split())
n, m=sp()
a, b, c=sp(), sp(), sp()

# B = defaultdict(int)
#
#
# B.update({g:len([1 for j in range(n) if (j+1)%g==0]) for g in set(b)})
# print B, 'b', n, [1 for j in range(n) if (j+1)%1]
# for i in range(m):
#     for j in range(n):
#         a[j]=(a[j]*c[i]**B[b[i]])%(10**9+7)
# print a

# B = {g: c[i] for g in set(b) for i in range(m) if }

# for j in range(n):
#     for i in range(m):
#         if b[i] <= (j+1) and (j+1)%b[i] == 0:
#             a[j]=(a[j]*c[i]) %(10**9+7)

B = Counter(b)

for i in range(n):
    for j in range(m/(i+1)):
        a[i*j]*=c[i]*B[i]


print ' '.join([str(a%(10**9+7)) for a in a])