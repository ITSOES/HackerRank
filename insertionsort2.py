def insertionSort(ar):
    t=ar[0]
    for i, e in enumerate(ar):
        j=0
        if e > t:
            t=e
        while e<t:
            j+=1
            ar[i-j]
        if i and ar[i+1] > t:
            ar[i]=ar[i+1]
        else:
            ar[i]=t
        print ' '.join(map(str, ar))


m=input()
ar=[int(i) for i in raw_input().split()]
insertionSort(ar)