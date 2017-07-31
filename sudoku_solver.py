import math,os, sys,random,time,turtle,operator
import datetime


def sudokuSolver(board):
    cols=[]
    for i in range(9):
        col=[]
        for j in range(9):
            col.append(board[j][i])
        cols.append(col)

    rows=[]
    for i in board:
        rows.append(i)
    blocks=[]
    for i in range(0,9,3):
        for j in range(0,9,3):
            block=[]
            for k in range(3):
                for l in range(3):
                    tmp=board[i+k][j+l]
                    if tmp==0:
                        return False
                    block.append(tmp)
            blocks.append(block)
    for i in (cols,rows,blocks):
        for j in i:
            if len(set(j))!=9:
                return False
    return True


print(sudokuSolver([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                         [6, 7, 2, 1, 9, 5, 3, 4, 8],
                         [1, 9, 8, 3, 4, 2, 5, 6, 7],
                         [8, 5, 9, 7, 6, 1, 4, 2, 3],
                         [4, 2, 6, 8, 5, 3, 7, 9, 1],
                         [7, 1, 3, 9, 2, 4, 8, 5, 6],
                         [9, 6, 1, 5, 3, 7, 2, 8, 4],
                         [2, 8, 7, 4, 1, 9, 6, 3, 5],
                         [3, 4, 5, 2, 8, 6, 1, 7, 9]]))
