import numpy as np

def validate(bo, n):
    for row in range (0,n):
        if sum(bo[row,])>1:
            return False

    for col in range (0,n):
        if sum(bo[:,col])>1:
            return False

    diags = [bo[::-1,:].diagonal(i) for i in range(-n+1,n)]
    diags.extend(bo.diagonal(i) for i in range(n-1,-n,-1))
    for x in diags:
        if len(x)>1:
            if sum (x)>1:
                return False

    return True

def solve (bo, col, n):
    if validate(bo,n):
        if bo.sum()==n:
            return True

        for row in range (0,n):
            bo[row,col] = 1
            if validate (bo,n):
                if solve(bo, col+1,n):
                    return True
                bo[row,col] = 0
            else:
                bo[row,col] = 0
    return False


board = np.zeros((8, 8))
if solve(board, 0, 8):
    print(board)
