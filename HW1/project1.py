# Programmer: Toni Hunter
# RUID: 187009925
# Date: 01/26/2022
#
# File: problem1.py
#
# Program Description: implement a function called multi_column_print with two parameters: a list
# L and an integer numcols. The list L has an arbitrary number of items, function should display
# the items in L equally distributed in numcols columns.neatly formatted and aligned by using string
# formatting with a suitable field width.

numcols = int(input("numcols: "))


def multi_column_print(L, numcols):
    count = 0
    for item in L:
        if count == numcols:  # once 1, 2, 3 ... count --> \n
            print(item, "\n")
            count = 0  # resets for new line
        else:
            count += 1
            print(("{:>10}".format(str(item))), end=" ")

L = [2**i for i in range(20)]
# L = [[1, 2, 3, "abc"], "hello", [10, 20, 30], "a", 45, 27, 99, 4.5, 3.14159]
multi_column_print(L, numcols)
