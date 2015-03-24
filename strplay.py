from time import time
from collections import OrderedDict, Counter,deque
from itertools import chain, izip
from pprint import pprint
import numpy
# from math import p
clok = time()

multiply=lambda x,y: x*y


from sys import setrecursionlimit
def combo7(s):
    import sys

    class Words:
        def __init__(self, words):
            self.s=words
            self.n=len(words)
            self.forwardArray=[1]
            self.backwardArray=[None]*self.n

        def buildPalindromeArray(self):
            # print self.n
            result=0
            # self.forwardArray[0]=1
            # self.backwardArray[-1]=1
            pre_0, pre_1= [0]*self.n, [1]*self.n

            for length in range(1, self.n-1):
                curr=[ pre_0[left+1]+2
                      if self.s[left] == self.s[left+length]
                      else max(pre_1[left], pre_1[left+1])
                            for left in range(self.n-length) ]
                self.forwardArray.append(curr[0])
                self.backwardArray[-length-1]=curr[-1]
                pre_0, pre_1=pre_1, curr
                # continue
                if length>=self.n>>1:
                    result=max(result,
                               self.backwardArray[length+1]*self.forwardArray[length],
                               self.forwardArray[self.n-length-2]*self.backwardArray[self.n-length-1])
                    if result>=(self.n-length)*(curr[-1]): break
            return result

        def findMaxScore(self):
            if self.n < 3:
                return int(self.n==2)
            result = self.buildPalindromeArray()
            if result: return result
            score=0
            print 'no result from first f'
            for i in range(1, self.n-1):
                score=max(score, self.forwardArray[i-1]*self.backwardArray[i])
            return score


    return Words(s).findMaxScore(), 'combo7'



    n=len(s)
    d=numpy.identity( n, int)
    ptop=numpy.arange(1,n+1)
    pside=numpy.arange(1, n+1)
    matched = 0+(d!=0)

    potential = numpy.identity(n,int).cumsum(axis=0).cumsum(axis=0)

    print potential.T
    print 'matched'
    print (matched & d==0)

    def get(i,j):
        # print 'ii,jj', i,j, d[i, j], 0 < i

        if j>i:
            d[i,j] = 2 + inside(i,j) if s[i]==s[j] else max(left(i,j),down(i,j))
            matched[i,j] = 1
        return d[i,j]
    def left(i,j): return d[i,j-1] or get(i, j-1)
    def down(i,j): return d[i+1,j] or get(i+1, j)
    def inside(i,j): return d[i+1,j-1] or get(i+1, j-1)

    def iget(i):
        return d[0,i] or get(0,i), d[i,n-1] or get(i,n-1)
    def m(A,B):
        return (A*B).max()

    def get_potential():
        temp = matched
        ptop=(numpy.arange(1,n)-d[0].min())
        pside=(numpy.arange(n-1,0,-1)-d[:,n-1].min())
        print numpy.arange(1,1+n), 'what?'
        print d[0]
        print ptop
        print pside
        print ptop*pside
        print 'm',m(ptop,pside)
        print 'pontential?\n', numpy.maximum(temp.cumsum(axis=1), temp[::-1].cumsum(axis=0)[::-1])
        print (matched | d != 0)
    result=0
    potential = (n-n/2)*(n/2)


    while result<potential:
        print 'pot',potential, n, (n-n/2),n/2
        print 'getpot', get_potential()
        print numpy.arange(1,n)
        print d[0]
        print iget(4)
        print d
        print get_potential()


        break


# new
def combo6(s):
    n=len(s)
    # r = range(n)
    # d={}
    d=numpy.identity(n,int) #[[0]*n]*n)
    # d=numpy.matrix(numpy.identity(n,int))
    # print(d)
    # d={(0,0):1}
    for e in xrange(1,n-1):
        pass
        # d[e,e]=0
        for i in xrange(n-e):
            # print s[i], s[i+e], s[:i],s[i],s[i+1:], s[:i+e],s[i+e], s[1+i+e:], 'e,(j,j+e)', e, (i,i+e),
            # if (j, j+e) in d:
            if s[i] == s[i+e]:
                # d[i, i+e]=2+d.pop((i+1, i+e-1))
                d[i, i+e]=2+d[i+1, i+e-1]
            else:
                # print d
                # print d[i:i+2,i+e-1:i+e+1].max()
                # d[i,i+e]=d.diagonal(offset=e-3)[i:].max()
                d[i, i+e]=max(d[i+1,i+e],d[i,i+e-1])
                # print
                # d.update({(i,i):1,(i,i-1):0})
            # print 'in d', d[i, i+e], d.get((i+1, i+e-1), 0), 'lll', d.get(i+1, i+e), d.get(i, i+e-1), 'i+1,i+e', i+1,i+e
        # t=d[1:, n-1]  ## The top row
        # s1=d[0, :-1]
        # print e, t*s1, t, s1

    # d2=numpy.identity(n,int)
    # d2=numpy.array([[1]+[0]*n]*n)
    # d2=numpy.array([[0]*n]+[[1]*n]+[[0]*(n)]*(n-1))
    # print  d2
    # for e in xrange(2,n-1):
    #     r=e
    #     print 'e',e
    #     for i in xrange(n-e):
    #         j=i
    #         # i, e=e, i
    #
    #         if s[i] == s[j+r]:
    #             d2[ e,i]=2+d[ e+1,i-1]
    #         else:
    #             d[e,i]=max(d[ e,i-1], d[ e+1,i])
    #         print d2
    #
    # print 'combo6'
    # print( d)
    # print d2
    # print '------------------------------'
    # print
    # rr =numpy.outer(d[:, n-1], d[0]).diagonal(offset=-1).max()
    t =d[1:, n-1] ## The top row
    s2 = d[0,:-1] ## The right side row
    # f = numpy.array([t,s])
    # print t*s2
    # print d
    # print numpy.outer(t,s)

    # print t, s, t[1:]*s[:-1]
    # print f, numpy.prod(f,axis=0)
    # print numpy.prod(d, axis=(0,1))
    return max(t*s2)
    return numpy.prod([t,s], axis=0).max()

    # for i in xrange(2, n):
    #     for j in xrange(n+1-i):
    #         if s[j] == s[j+i-1]:
    #             d[j][j+i]=2+d[j+1][j+i-1]
    #         else:
    #             d[j][j+i]=max(d[j][j+i-1], d[j+1][j+i])
    # for
    return max(d[0, v]*d[v+1, n-1] for v in range(n-1))
    # return max(d.get((0,i),0)*d.get((i+1,n),0) for i in range(n))


# pprint=lambda x:None
def other(s):
    n=len(s)
    d=[[int(i==j) for i in xrange(n)] for j in xrange(n)]
    # d={(i,j):cmp(i,j) for i in xrange( n+1) for j in xrange(i,n+1)}
    # print n
    # for i in xrange(2, n):
    #     for j in xrange(n+1-i):
    #         # print 'i,j', i,j, 'd[j][j+i]', d[j][j+i], 'j+i',j+i , 'j+1, j+i-1', j+1, j+i-1, 'in d', d[j+1][j+i-1]
    #         if s[j] == s[j+i-1]:
    #             d[j][j+i]=2+d[j+1][j+i-1]
    #         else:
    #             d[j][j+i]=max(d[j][j+i-1], d[j+1][j+i])
    for i in xrange(1, n-1):

        for j in xrange(n-i):
            # print 'i,j', i,j, 'd[j][j+i]', d[j][j+i], 'j+i',j+i , '[j+1, j+i-1]', (j+1, j+i-1), 'in d', d[j+1][j+i-1]
            if s[j] == s[j+i]:

                d[j][j+i]=2+d[j+1][j+i-1]
            else:
                d[j][j+i]=max(d[j][j+i-1], d[j+1][j+i])
            # pprint(d)
            # print 'i,j', (i,j), 'max', d[j][j+i], 'left', j,j+i-1, d[j][j+i-1], 'down', j+1,j+i, d[j+1][j+i],'\n'
        # print d[0][i]*d[i][n]

    # pprint(d)
    # gn=list((d[0][i], d[i+1][n-1]) for i in xrange(n-1))
    # for i,j in gn:
    #     print(i,j), i*j

    m=max(d[0][i]*d[i+1 ][n-1] for i in xrange(n-1))
            # print 'i,j', i,j, 'A,B', d[0][i],d[j][n], 'm', m
        # d[0][i]=-1
        # pprint(d)
    return m

def combo5(s):
    n=len(s)
    d={(i, i): 1 for i in range(n)}
    result=a=0
    works={0:0}
    for e in xrange(1,n-1):
        for i, j in izip(xrange(n), xrange(e, n)):
            freeup=d.pop((i+1, j-1), 0)
            # if e: [i, j]=1
            if s[i] == s[j]:
                d[i, j]=2+freeup
            else:
                d[i, j]= max(d.get((i, j-1)), d.get((i+1, j)))
        # continue
        if e>=n/2:
            a = d[0,e]*d[e,n-1]
            bi, bj =  works.pop(n-e,0), d[n-e, n-1]
            result =max(result, a, bi*bj)
            # print 'a',a, result, 'e',e, 'g3', bi, 'e', e, 'n-e', n-e, works.get(n-e, 0), d[n-e, n-1]
            # print  max(works), g3, works
            if result>=a and result>=bj*max(works):
                # continue
                return result
        elif d[0,e]>a:works[e]=a=d[0,e]
        # if result/g2>n-e:
    # pass
    # return
    # print(d)
    # print works, 'woorks'
    return result or max(d[0,v]*d[v+1,n-1] for v in range(n-1))
def combo4(s):
    n=len(s)
    d=OrderedDict()
    factors = OrderedDict()
    l=deque()
    here = range(n)
    iexplored = set()
    ibest=0
    for i in chain(*zip(xrange(n/2, n), xrange(n/2))):
        iexplored.add(i)
        for j in reversed(range(i, n)):
            if s[i] == s[j]:
                ew =s[i+1:j]
                if ew:
                    l.append((ew,2-int(i==j), len(ew),(i+1,j+1)))
                    best=2
                else:
                    best=int(i!=j+1)
                # print i,j
                while l:
                    print l, (i,j)
                    sub, cur, n2,(k,o) = l.pop()
                    if sub==sub[::-1]:
                        if cur+n2>best:
                            best=cur+n2
                            d[k,o]=n2
                        continue
                    if (k,o) in d:
                        if d[k,o]+cur>best:
                            best=d.get((k, o), 0)+cur
                        print 'k,o',k,o,'dd', d.get((k, o)), cur
                        continue
                    if cur+n2<=best: continue
                    for I in xrange(n2):
                        for J in reversed(range(I, n2)):
                            assert I<=J
                            if I==J:
                                if cur+1>best:
                                    best =1+cur
                            elif sub[I] == sub[J]:
                                ew=sub[I+1:J]
                                # print ew,'eeee',len(s[I+1:J]), I, J
                                if ew:
                                    l.append((ew, 2+cur, len(ew),(k+I+1,k+len(ew)+I)))
                                elif cur+1 > best:
                                    best=1+cur
                d[i,j]=best
    print n, 'n'
        # factors[i,j]
    return d


s=test0="jcaabdovmuiwsjkskeyifhfjxebwqbuqkndxmrxpqdbnpecgdh"
test1="aacdcbdccdccbacadcdcbbbdbcaacabddbcaddbccdcaccadbadcdcdcbaabcadbdcabdbcccbddcdabcaadcdadcacbdbccccbcacccdbacbddbacbccdadddbccdbddcabbbcccdddadddccdbddabbddcaadacaacdddbcbbccdadadbdbbcaaabccabdaaddadaa"
test2="lklddhkidgffdkhhkcjkefjlejhkkfihgiiiiddkcihejcdjdkfhjdhkjffjjdcghidgkicffelfekgkljjfclcffjdjgeeeieijhfckcecgfgldghjeicldhfidecglldhjelhfcjeifhjedgflihklfgjjhhcfgglldlhfjlgjicihfigcegifechgkihcchjceifhihjciggihjhgciedgfeffhiegijehjlhkclehiikeegjjfhdfdhkcgglilhhieedgdkfkfhfgekjjfklfgfjhfelekljdkfejgjccggjhcjhcjldcefekgghgkeklkgcfefchegkhgceljkklcgcfllchlddcghhggfhfffhkdefgidfhjlikcidclcedekhghlgejkijkfkfigfccekjcieckkeljhfekdfgidhlchfhlfllldfdfehhdikhlfjjeflkjdhhkkjjhdeecejfchklfhkeieljjhgigdllfidleijghlijkkiijligdfcldfiehhkhglikcggkddhkfgchhjhhkfefejghklfeichcdkfejicfdccjicdkdjigccjlhhkecceghhijgcekefliijilhgijicjhgjkkclcgefhjdjhhjkkkjgkdcfjffleickffdcdhcjcfflgdchfdfkjdecleheiegeehkjgcdflekjfikhhkfikdkejefkelkceklhlcckgecleldjhckiekchkiklecljjgggklighcfjdcgefcgcdlicfhlfgckhfjekejelgckgldfifjifccdckfdiflgkicigfjdihdldcflciicgclkdkgekfigklcjkdjecjecehhkkgifgcgifijljejjckfjeicghfifehjedclcjidicglhjfcdcehhlldjgjjckjlchgdeklkfcfcgggiehelehgjhkhhjigidiicjhcifkekjdkjhddhiicjkkkdjffdglhgckkcgejcihikjcifigdfgfiicecedckglgdfjkdkcelifhjcflhllfgceflilgkcfeldjhljcekljhgfgkgcffgkcddelkgiifhggjkifhceikgcfidfljfkghllgikllkdecikjhgkehkgdlehjkkjgjhjfhhjilhkhlkiedjlkkfkhhjlhdjdccdkcfihcgghigfgkcdkcjjjghfelcjgigfccikigijcdkgicgeedhffhfkgkcjdcjkgfjehfgjiefickchgcfchkcldjfhlfilfkfldhekhjdijkhglhgkiilihkhgdehjkigjfdfjgghckkddjcffcjiciidhggilichkjldljegjkfdjfcejldegjeecfljfldldkiidkffclkedljheejhgjceeglhlkflefhdgjfdcileecigeccgdifcicfkhliflfhhgjecdfccgdigffkgdkilfijceelhfljfijiccdklkclccgilgkhekggdcgjhjccdkldccicckkdcchgghgjhdfghfclclikkdfdffieflkcchdjdgcdjilgdlkegikceghikfdffeglkhkfilchhekhdicchkclciceddccekihcfhfgjcfkghceigfjglfdheciehcdfhcgfkdiiclhiceifcgidejcklidiieckkfdkkkejigljhgffgjjldffddfjdgcghkeicidgdhcjkjehgdhehlhghljfddgiiclgeijcikeckedffgihfledkfcfefffldkfkhdlkfcdhlikefhkdlflgcgkickfffhigfggkfccjdjedkedigjdhjcgcggfijgjgdkejhijigfgkfljldhdffkkkliiedhiegkfjkgigfdcdegeilfkcegekglcjkidjffceiekdkhedkkfefjidhfhgkiiillielhdfgclflcjhkjhcldfhcejcdkdlkckhdfdlchilcgkheliflkkdkcggilejfdciekhgldggffgkfjejeljhfkljkgjfchcfdlihjjihgigilfjcjgcjjcflhjdleijeghgielckifikejglkekcfjcljdeeckddkjgkfidlcfkgdjjclfjlcfjjekffhickllfigddjfdcgdllgekjkjhldikighjdecfhhigchleechihjkhlkiihdfcjcjhjliedjhligediehihecicckccgghdilffifkgflljlckdkjcikggchgggfidchjijhjhcfefdglkidjgefcegkdcgfjckejgjdgihhdhflceciilfkkckdfgihcefllgceihgjecikceldgcfjcjgjhllkelgfelhhefhkdccdgigdiddccehjjecjdlkjcllhegfgllflcgcccgcfdkhdjejikcfgejhkdeldkhcflfcgdhhfdkikkkhkhgegkcjggcjlifkedcfciidkghhlhjcjhjcdddilkeficdfcekidfecldddjf"
test3='wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwdfvadscqwerwc'
test="eeegeeksforskeeggeeks"
test5="abaabbbbfdgsaaaaaaaaa"
test4=[raw_input() for x in range(3)][-1]


test=test

clok1 = time(); d1=other(test); clok1 = time()-clok1
clok2 = time(); d2 = combo5(test3); clok2 = time() - clok2
clok3=time();   d3=combo6(test);clok3=time()-clok3
clok4=time();   d4=combo7(test2);clok4=time()-clok4

print test
# print 'dddd', dd

dddd = {}
def combo3(s):
    n = len(s)
    d = {}
    def f(i,j,ee=0):
        print ee, i, j
        assert i<=j
        n2 = len(s)
        if s == s[::-1]:
            return n2
        result = set([1])
        for I in range(i,j):
            for J in range(I,j+i-I):
                if s[I]==s[J]:
                    # print'I,J', I,J
                    result.add(2+f(I,J,ee+1))
        return max(result)

    for i in range(n):
        for j in range(i,n):
            if s[i]==s[j]:
                d[i,j]=f(i,j)

    return d



# test2="aacdcbdccdccddadaa"
# ans2 = combo3(test2)
# print 'combo3', ans2
# print 'ans2', f1(ans2)
# gggg=OrderedDict(x for x in combo(test))


def combo2(iterable, r):
    pool=tuple(iterable)
    n=len(pool)
    if r > n:
        return
    indices=range(r)
    j=r
    print 'r', r
    b = tuple(pool[i] for i in indices)
    if b==b[::-1]: yield (0,j)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i+n-r:
                break
        else:
            return
        indices[i]+=1
        for j in xrange(i+1, r):
            indices[j]=indices[j-1]+1
        b = tuple(pool[i] for i in indices)
        if b==b[::-1]:
            yield (indices[0],indices[-1])


def combo(iterable):
    pool=tuple(iterable)
    n=len(pool)
    cc = counts = Counter()
    print "string", iterable
    for i in xrange(n):
        coun = 0
        for j in xrange(i, n):
            if pool[i]!=pool[j]:
                continue
                # cc.update([(i,j)])
            count = best = 0
            print i,j,'i,j'
            for I in range(i,j+1):
                for J in reversed(range(I,j+1-coun)):
                    print I,J
                    count+=1
                    if pool[I]==pool[J]:
                        print I,J, 'I,J'
                        cc.update([(i, j)])
                        coun = count
                        break
                else:
                    # pass
                    coun = count = 0


            if False and pool[i]==pool[j]:
                best=0
                i2, j2 = i, j
                ii,jj= i2,j2
                counts = Counter()
                count=0
                I, J=i2, j
                l=[]
                while J-I>=0:
                    while J >= I:
                        print pool[I], pool[J], 'I,J', I, J, 'count', count, 'i,j', (i, j)
                        if J == I:
                            count+=1
                            # jj,ii = J,I
                            break
                        elif pool[I] == pool[J]:
                            count+=2
                            I+=1
                            ii=I
                            jj=J-1
                            counts[I,J-1]=counts[J-1]=count
                            if counts[I,J]<count: counts[i2,J]=count
                        J-=1
                    i2+=1
                    # counts[I,J+1]=count
                    # counts[ii,jj]=count

                    I,J=i2,j2-count%2
                    # (I,J),count = counts.popitem()
                    if count>best:best=count
                    count=counts[J]
                    # count=
                # print(ss, count)
                yield (i, j), best
                # break
            if counts:print counts, (i,j)
    for c in cc.items(): yield c
    # ggg=Counter((i, j) for i in range(n) for j in range(i, n) if pool[i] == pool[j]
    #                     for I in range(i,j+1)
    #                     for J in range(I, j+1-(I-i)) if pool[I]==pool[J])
    # print 'gg',ggg
    # print pool

# def combo(s):
#
#     for i in range(len(s)):
combo2 = (lambda f:lambda s: OrderedDict((x, r) for r in range(1,len(s)) for x in f(s, r)))(combo2)
if __name__ == '__main_':
    test="heyeifhfjxe"
    gg= combo2(test)
    # gggg=OrderedDict(x for x in combo(test))
    print 'x', gg
    print 'f1', f1(gg), 'string', test
    kk=combo2(test)
    print '-------', s
    print kk, '\ncombo2', f1(kk)
import re


# pool="eyifhfjxe"
# n=len(pool)
# ggg=Counter((i, j) for i in range(n) for j in range(i, n) if pool[i] == pool[j] for I in range(i, j+1) for J in range(I, j+1-(I-i)) if pool[I] ==pool[J])
# ggg=OrderedDict(sorted(ggg.items()))
# print 'ggg', ggg

s=pool=raw_input()
# print s
n=leng=len(s)
temp=[]
palins=OrderedDict()
# palins=Counter((i, j) for i in range(n) for j in range(i, n) if pool[i] == pool[j]
#                     for I in range(i, j+1)
#                     for J in range(j-(I-i),I-1,-1) if pool[I] ==pool[J])
# palins=OrderedDict(sorted(palins.items()))
# for r in sorted(range(1,leng), key=lambda x:abs(x - leng/2)):



if __name__=="__main__c":
    for ij, count in combo(s):
        palins[ij]=count
    print

    print palins
    print f1(palins), 'll'
print
clok = time()-clok
print 'cloks',clok
print 'other', clok1, d1, '\ncomb5', clok2, d2
print 'new  ', clok3, d3
print 'newer', clok4, d4