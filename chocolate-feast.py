for _ in range(input()):
    N, C, M=[int(x) for x in raw_input().split(' ')]
    
    answer=wrappers=N//C
    while wrappers >= M:
        wrappers-=M-1
        answer+=1
    
    print answer