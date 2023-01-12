A = ""
B = ""
m, n = 0, 0
match,mismatch,c=2,-1,-1

def max(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
def ScoringMatrix():
    
    import numpy as np
    max_score=0
    max_pos_i, max_pos_j = 0, 0
    m, n = len(A), len(B)
    M = [[0 for j in range(m + 1)] for i in range(n + 1)]
    
    for i in range(m + 1):
        M[i][0] = 0
    for j in range(n + 1):
        M[0][j] = 0

    for j in range(1, n + 1):
        for i in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                M[i][j] = M[i - 1][j - 1] + match
            else:
                M[i][j] = max(M[i - 1][j - 1] + mismatch,
                              M[i - 1][j] + mismatch,
                              M[i][j - 1] + mismatch)
            if M[i][j] > max_score:
                max_score = M[i][j]
                max_pos_i, max_pos_j = i, j
                

    for i in range(m):
        print(B[i],end="  ")
    print("\n  ", end = "")
    for i in range(n+1):
        if i > 0:
            print(A[i - 1], end = " ")
        for j in range(m+1):
            print(M[i][j], end = "  ")
        print()

    




if __name__ == "__main__":
    A='tgggctcgtaaactta'
    B='cgcctcgccagtccga'
    ScoringMatrix()