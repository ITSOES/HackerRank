def nextMove(length, b, board):
    if 'b' not in board:
        return 'CLEAN'

    def coord(pos):
        return divmod(pos, length)
    def dist(p1,p2):
        x1,y1=coord(p1)
        x2, y2=coord(p2)
        return abs(x1-x2)+abs(y1-y2)
    pp=board.replace('d', '-', 1)
    you, d=map(board.index, 'bd')
    while 'd' in pp:
        p2=pp.index('d')
        if dist(d,you) > dist(p2,you):
            print dist(d,you), dist(d,p2), coord(you),coord(d), coord(p2)
            print( 'yyy', d,you,p2, 'tyiuyf')
            you=p2
        else:
            pp=pp.replace('d', '-', 1)

    if you >= d+length:
        return 'UP'
    elif you <= d-length:
        return 'DOWN'
    elif d%length > you%length:
        return 'RIGHT'
    else:
        return 'LEFT'

if __name__ == "__main__":
    b=raw_input()

    board=''.join([raw_input() for i in range(5)])

    print nextMove(len(board)/5, b, board)