def displayPathtoPrincess(length, g):
    you, girl=map(g.index, 'mp')
    while you != girl:
        if you >= girl+length:
            print 'UP'
            you-=length
        elif you <= girl-length:
            print 'DOWN'
            you+=length
        elif girl%length > you%length:
            print 'RIGHT'
            you+=1
        else:
            print 'LEFT'
            you-=1


# h=int(input())
# s=''
# for i in xrange(h):
#     s+=raw_input()

# displayPathtoPrincess(len(s)/h, s)
print 'ooo'.replace('o','n')