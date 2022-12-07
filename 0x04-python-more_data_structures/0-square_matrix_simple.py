#!/usr/bin/python3
def square_matyrix_simple(matrix=[]):
    tmp = []
    for x in matrix:
        tmp.append(list(map(lambda x: x**2, x)))
    return(tmp)
