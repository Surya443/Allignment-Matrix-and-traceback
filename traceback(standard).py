def traceback(M,x,y):
    diag, up, left = 1, 2, 3
    move = nmov(M,x,y)
    global alignA
    global alignB
    if move == 1:
        print(M[x][y])
        alignA += A[x-1]
        alignB += B[y-1]
        traceback(M,x-1,y-1)
    elif move == 2:
        print(M[x][y])
        alignA += A[x-1]
        alignB += '_'
        traceback(M,x-1,y)
    elif move==3:
        print(M[x][y])
        alignA += '_'
        alignB += B[y-1]
        traceback(M,x,y-1)
    if(move==0):
        alignA += B[x-1]
        alignB += A[y-1]
        alignA = alignA[::-1]
        alignB = alignB[::-1]
        print(alignA)
        print(alignB) 