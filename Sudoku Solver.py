import numpy

def possiblity_check(y,x,n):
    global sudoku_puzzle
    for i in range(9):
        if sudoku_puzzle[y][i] == n:
            return False
        if sudoku_puzzle[i][x] == n:
            return False
    x0=(x//3)*3
    y0=(y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if sudoku_puzzle[y0+i][x0+j] == n:
                return False
    return True

def solution():
    global sudoku_puzzle
    for y in range(9):
        for x in range(9):
            if sudoku_puzzle[y][x] == 0:
                for n in range(1,10):
                    if possiblity_check(y,x,n):
                        sudoku_puzzle[y][x] = n
                        solution()
                        sudoku_puzzle[y][x] = 0
                return
    print("\n\nRequired Solution:\n")
    print(numpy.matrix(sudoku_puzzle))

sudoku_puzzle = []

try:
    for i in range(9):
        temp=[int(x) for x in input().split()]
        if len(temp) != 9:
           raise "Invalid Length"
        sudoku_puzzle.append(temp)
except:
    print("Error Occured")
else:
    solution()