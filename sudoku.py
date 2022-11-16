# -*- coding: utf-8 -*-
"""
Created on Wed Jan 04 08:13:32 2017
Formulates & solves sudoku as a CSP
@author: Fabian C. Annaheim
"""

import sys
import constraint as csp

def printSudoku(riddle):
    print("- - - - - - - - - - - - -")
    for row in range(9):
        line = ["|"]
        for col in range(9):
            line.append(str(riddle[row][col]))
            if (col + 1) % 3 == 0:
                line.append("|")
        print(*line)
        if (row + 1) % 3 == 0:
            print("- - - - - - - - - - - - -")

riddle = [[0, 0, 0, 2, 0, 0, 0, 6, 3],
          [3, 0, 0, 0, 0, 5, 4, 0, 1],
          [0, 0, 1, 0, 0, 3, 9, 8, 0],
          [0, 0, 0, 0, 0, 0, 0, 9, 0],
          [0, 0, 0, 5, 3, 8, 0, 0, 0],
          [0, 3, 0, 0, 0, 0, 0, 0, 0],
          [0, 2, 6, 3, 0, 0, 5, 0, 0],
          [5, 0, 3, 7, 0, 0, 0, 0, 8],
          [4, 7, 0, 0, 0, 1, 0, 0, 0]]

# Row and column indices
rownames = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
colnames = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

# Array representing rows
rows = []
for i in rownames:
    row = []
    for j in colnames:
        row.append(i + j)
    rows.append(row)

# Array representing columns
cols = []
for j in colnames:
    col = []
    for i in rownames:
        col.append(i + j)
    cols.append(col)

# Array representing 3x3 boxes
boxes = []
for x in range(3):
    for y in range(3):
        box = []
        for i in range(3):
            for j in range(3):
                box.append(rownames[x * 3 + i] + colnames[y * 3 + j])
        boxes.append(box)

# Create CSP
sudoku = csp.Problem()

# Add variables
for row in range(9):
    for col in range(9):
        sudoku.addVariable(rows[row][col], [1, 2, 3, 4, 5, 6, 7, 8, 9] if riddle[row][col] == 0 else [riddle[row][col]])

# Constraint to assure different values for all digits
constraint = csp.AllDifferentConstraint()

# Add constraint to all rows
for row in rows:
    sudoku.addConstraint(constraint, row)

# Add constraint to all columns
for col in cols:
    sudoku.addConstraint(constraint, col)

# Add constraint to all 3x3 boxes
for box in boxes:
    sudoku.addConstraint(constraint, box)

# Print riddle
print("\nRiddle:")
printSudoku(riddle)

# Print solution
for solution in sudoku.getSolutions():
    print("\nSolution:")
    solved = riddle
    for row in range(9):
        for col in range(9):
            if solved[row][col] == 0:
                solved[row][col] = solution[rownames[row] + colnames[col]]
    printSudoku(solved)
