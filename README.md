# Sudoku as Constraint Satisfaction Problem

This repository contains a sudoku solver which is implemented by formulating a sudoku riddle as <b>constraint satisfaction 
problem (CSP)</b>. A CSP consists of a set of variables, their ranges of values, and the conditions that establish 
links between the variables and thereby determine which combinations of values of the variables are allowed. A variety of 
problems from computer science, mathematics, and other application areas can be formulated in this way. This implementation
relies on the python-constraint [library](https://pypi.org/project/python-constraint/) developed by Gustavo Niemeyer. It
is able to take each possible sudoku configuration of a 9x9 riddle and solve it instantly. 
