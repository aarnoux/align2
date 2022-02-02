#!/usr/bin/env python3
# -*- coding utf-8 -*-

import sys
import numpy as np

def matrice_creation(n,m,A,B):
    M = np.zeros((n+1,m+1))
    X = np.array([[]])
    Y = np.array([[]])
    for i in range(n):
        X = np.append(X,[A[i]])
    for j in range(m):
        Y = np.append(Y,B[j])
    return M,X,Y

def matrice_initialization(n,m,M):
    g = -2
    for i in range (0,n+1):
        M[i,0]=(i*g)
    for j in range (0,m+1):
        M[0,j]=j*g
    return M

def firstLine(X,Y,M,m,n):
    match = 4
    mismatch = -3
    for j in range(1,n+1):
        for i in range(1,m+1):
            value = max(M[j-1,i-1],M[j,i-1],M[j-1,i])
            if X[j-1] == Y[i-1]:
                value += match
            else:
                value += mismatch
            M[j,i] = value
    return M

def main():
    A = sys.argv[1]
    B = sys.argv[2]
    n = len(A)
    m = len(B)
    M,X,Y = matrice_creation(n,m,A,B)
    M = matrice_initialization(n,m,M)
    M = firstLine(X,Y,M,m,n)
    print(M)

if __name__ == "__main__":
    main()
