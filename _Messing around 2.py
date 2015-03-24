from collections import defaultdict, Counter, OrderedDict
from pprint import pprint
k="qqqqqgrr"
n=len(k)

print k
print k[::-1]
d=defaultdict(list)
d2=defaultdict(list)
d3=Counter()
for i,c in enumerate(k):
    for j, c2 in enumerate(k[i:]):
        pass
        if c is c2:
            d[i].append(j+i)
            d2[j+i].append(i)

pprint(dict(d))
# pprint(dict(d2))
# l=''
# for i in d.copy():
#     for j in d[i]:
#         # print k[i:j+1]
#         # d3[i]+=(d[j].pop()!=j)+1
#         d3[i,j]+=2
print d3
# pprint(dict(d))
ggg=OrderedDict(((i, j),1+(i!=j))
                            for e in xrange(n-1)
                            for i, j in zip(xrange(n), xrange(e, n))
                            if k[i]==k[j])
g=Counter(ggg)
for i,j in ggg.copy():
    pass
    con = [0]
    for i1,j2 in ggg:
        if j2-i1<j-i and j>i1>i:
            print i,i1,j2,j
            con.append(ggg[i1,j2])
    g[i,j]+=max(con)
    # ggg.pop((i,j))

lh={}
rh={}
for (x,y),v in g.items():
    if x==0:
        lh[y]=g[x,y]
    elif y==n-1:
        rh[x]=v



# [d1*d2 for d1 ]
print ggg
g.update()
print g
print lh
print rh
print max(l*r for y, l in lh.items() for x, r in rh.items() if y<x)